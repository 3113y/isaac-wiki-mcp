"""
Wiki Builder — converts Isaac API data JSON into structured wiki markdown pages.

Converts ``processed_apis.json`` (class-organized) + ``rag_knowledge_base.json``
(per-method versions/modifiers) into an llmwiki-style file tree::

    wiki/
      classes/   — one markdown file per API class
      enums/     — enum reference pages (from Isaac-API/docs/enums/)
      tutorials/ — how-to guides (from Isaac-API/docs/tutorials/)
      index.md   — global navigation with [[wikilinks]]
      llms.txt   — AI-consumable summary (llmstxt.org spec)

Cleaning performed during conversion:
- Deduplicates class_enhancement (stored once per class, not per method)
- Strips MkDocs markdown artifacts from signatures
- Filters placeholder summaries ("方法说明" boilerplate)
- Generates [[wikilinks]] cross-references from return/parameter types
"""

from __future__ import annotations

import json
import re
import shutil
from collections import defaultdict
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Known Isaac API class hierarchy (for inheritance detection)
# ---------------------------------------------------------------------------
_ENTITY_SUBCLASSES = {
    "EntityBomb", "EntityEffect", "EntityFamiliar", "EntityKnife",
    "EntityLaser", "EntityNPC", "EntityPickup", "EntityPlayer",
    "EntityProjectile", "EntityTear",
}

_GRIDENTITY_SUBCLASSES = {
    "GridEntityDoor", "GridEntityPit", "GridEntityPoop",
    "GridEntityPressurePlate", "GridEntityRock", "GridEntitySpikes",
    "GridEntityTNT",
}


def _detect_parents(class_name: str) -> list[str]:
    """Return parent class(es) for a given Isaac API class."""
    if class_name == "Entity":
        return []
    if class_name in _ENTITY_SUBCLASSES:
        return ["Entity"]
    if class_name == "GridEntity":
        return []
    if class_name in _GRIDENTITY_SUBCLASSES:
        return ["GridEntity"]
    return []


# ---------------------------------------------------------------------------
# Signature cleaning
# ---------------------------------------------------------------------------
_MKDOCS_ARTIFACT = re.compile(r"\{:\s*\.copyable\s+aria-label=['\"][^'\"]*['\"]\s*\}")
_LINK_PATTERN = re.compile(r"\[([^\]]+)\]\([^)]+\.md\)")


def clean_signature(sig: str) -> str:
    """Strip MkDocs artifacts and simplify markdown links from a signature.

    ``[BitSet128](BitSet128.md) BitSet128(...) {: .copyable aria-label='...'}``
    becomes ``BitSet128 BitSet128(...)``.
    """
    sig = _MKDOCS_ARTIFACT.sub("", sig)
    # Replace [Type](Type.md) → Type
    sig = _LINK_PATTERN.sub(r"\1", sig)
    # Collapse whitespace
    sig = " ".join(sig.split())
    return sig


def _extract_class_refs(text: str, known_classes: set[str]) -> set[str]:
    """Find references to known class names in arbitrary text.

    Used on descriptions and summaries to discover semantic cross-references.
    """
    found: set[str] = set()
    for cls in known_classes:
        if cls in text:
            found.add(cls)
    return found


def _extract_sig_class_refs(signature: str, known_classes: set[str]) -> set[str]:
    """Extract class names referenced in a cleaned method signature.

    Looks for patterns like: ``ClassName method(... ClassName ...)``.
    """
    found: set[str] = set()
    words = re.findall(r"\b([A-Z][a-zA-Z0-9_]*)\b", signature)
    for word in words:
        if word in known_classes:
            found.add(word)
    # Also check linked patterns that survived cleaning
    linked = _LINK_PATTERN.findall(signature)
    for link in linked:
        if link in known_classes:
            found.add(link)
    return found


def _is_placeholder_summary(summary: str) -> bool:
    """Detect boilerplate / placeholder summaries that add no signal."""
    if not summary or not summary.strip():
        return True
    s = summary.strip()
    if s.endswith("方法说明") or s.endswith("方法说明。"):
        return True
    if s in {"暂无描述", "待补充", "待补充。"}:
        return True
    return False


# ---------------------------------------------------------------------------
# Wiki page renderers
# ---------------------------------------------------------------------------

def _render_frontmatter(meta: dict[str, Any]) -> str:
    """Render YAML-style frontmatter block."""
    lines = ["---"]
    for key, value in meta.items():
        if isinstance(value, list):
            lines.append(f"{key}: [{', '.join(value)}]")
        elif isinstance(value, str):
            lines.append(f"{key}: {value}")
        else:
            lines.append(f"{key}: {value}")
    lines.append("---\n")
    return "\n".join(lines)


def _render_class_page(
    class_name: str,
    methods: list[dict[str, Any]],
    class_enhancement: dict[str, Any],
    method_enhancements: dict[str, dict[str, Any]],
    known_classes: set[str],
    versions_map: dict[str, list[str]],
    modifiers_map: dict[str, list[str]],
) -> str:
    """Render a complete class wiki page as markdown.

    Args:
        class_name: e.g. "EntityPlayer"
        methods: list of method dicts from processed_apis.json
        class_enhancement: class-level summary + use_cases + key_methods
        method_enhancements: {method_id: {summary, use_cases, key_methods}}
        known_classes: all class names (for wikilink generation)
        versions_map: {method_id: [versions]} from rag_knowledge_base
        modifiers_map: {method_id: [modifiers]} from rag_knowledge_base
    """
    parents = _detect_parents(class_name)
    class_summary = class_enhancement.get("summary", "")
    class_use_cases = class_enhancement.get("use_cases", [])
    class_key_methods = class_enhancement.get("key_methods", [])

    # Collect all cross-references for this class
    all_refs: set[str] = set()

    lines: list[str] = []

    # --- Frontmatter ---
    versions_all: set[str] = set()
    for vlist in versions_map.values():
        versions_all.update(vlist)

    fm = {
        "title": class_name,
        "category": "class",
        "dlc_versions": sorted(versions_all) if versions_all else ["All DLCs"],
        "method_count": len(methods),
    }
    lines.append(_render_frontmatter(fm))

    # --- H1 ---
    lines.append(f"# {class_name}\n")

    # --- Summary ---
    if class_summary and not _is_placeholder_summary(class_summary):
        lines.append("## Summary\n")
        lines.append(f"{class_summary}\n")

    # --- Inheritance ---
    if parents:
        lines.append("## Inheritance\n")
        for p in parents:
            lines.append(f"- Inherits from: [[{p}]]")
            all_refs.add(p)
        lines.append("")

    # --- Children (who inherits from this) ---
    if class_name == "Entity":
        children = sorted(_ENTITY_SUBCLASSES)
    elif class_name == "GridEntity":
        children = sorted(_GRIDENTITY_SUBCLASSES)
    else:
        children = []
    if children:
        lines.append("- Subclasses:")
        for c in children:
            lines.append(f"  - [[{c}]]")
            all_refs.add(c)
        lines.append("")

    # --- Related Types ---
    related: set[str] = set()
    for method in methods:
        sig = clean_signature(method.get("signature", ""))
        related.update(_extract_sig_class_refs(sig, known_classes))
        desc = method.get("description", "")
        related.update(_extract_class_refs(desc, known_classes))
        mid = method.get("id", "")
        me = method_enhancements.get(mid, {})
        me_summary = me.get("summary", "")
        related.update(_extract_class_refs(me_summary, known_classes))

    related.discard(class_name)
    related.difference_update(parents)
    all_refs.update(related)

    if related:
        lines.append("## Related Types\n")
        for r in sorted(related):
            lines.append(f"- [[{r}]]")
        lines.append("")

    # --- Key Methods (quick nav) ---
    if class_key_methods:
        lines.append("## Key Methods\n")
        for km in class_key_methods:
            if any(m.get("name") == km for m in methods):
                lines.append(f"- [[#{km}|{km}]]")
            else:
                lines.append(f"- {km}")
        lines.append("")

    # --- Methods ---
    # Group: constructors, operators, functions
    constructors = [m for m in methods if m.get("name") == class_name or m.get("name", "").startswith("__")]
    operators = [m for m in constructors if m.get("name", "").startswith("__")]
    ctors = [m for m in constructors if not m.get("name", "").startswith("__")]
    functions = [m for m in methods if m not in constructors]

    lines.append("## Methods\n")

    def _render_method_section(title: str, method_list: list[dict]) -> None:
        if not method_list:
            return
        lines.append(f"### {title}\n")
        for method in method_list:
            _render_method_entry(
                method, method_enhancements, versions_map, modifiers_map,
                known_classes, lines, all_refs,
            )

    _render_method_section("Constructors", ctors)
    _render_method_section("Operators", operators)
    _render_method_section("Functions", functions)

    # --- See Also ---
    if all_refs:
        lines.append("## See Also\n")
        for ref in sorted(all_refs):
            lines.append(f"- [[{ref}]]")
        lines.append("")

    return "\n".join(lines)


def _render_method_entry(
    method: dict[str, Any],
    method_enhancements: dict[str, dict[str, Any]],
    versions_map: dict[str, list[str]],
    modifiers_map: dict[str, list[str]],
    known_classes: set[str],
    lines: list[str],
    all_refs: set[str],
) -> None:
    """Render a single method entry within a class page."""
    name = method.get("name", "?")
    mid = method.get("id", "")
    raw_sig = method.get("signature", "")
    sig = clean_signature(raw_sig)
    desc = method.get("description", "")

    me = method_enhancements.get(mid, {})
    me_summary = me.get("summary", "")
    me_use_cases = me.get("use_cases", [])
    me_key_methods = me.get("key_methods", [])

    versions = versions_map.get(mid, [])
    modifiers = modifiers_map.get(mid, [])

    lines.append(f"### {name} {{#{name}}}\n")

    if sig:
        lines.append(f"```\n{sig}\n```\n")
    elif raw_sig:
        lines.append(f"```\n{raw_sig}\n```\n")

    badges: list[str] = []
    if versions:
        badges.append(f"DLC: {', '.join(versions)}")
    if modifiers:
        badges.append(f"Modifiers: {', '.join(modifiers)}")
    if badges:
        lines.append(f"*{' | '.join(badges)}*\n")

    if me_summary and not _is_placeholder_summary(me_summary):
        lines.append(f"{me_summary}\n")

    if desc and desc.strip():
        lines.append(f"{desc.strip()}\n")

    if me_use_cases:
        lines.append("**Use Cases:**\n")
        for uc in me_use_cases:
            lines.append(f"- {uc}")
        lines.append("")

    refs = _extract_sig_class_refs(sig, known_classes)
    refs.update(_extract_class_refs(desc, known_classes))
    refs.update(_extract_class_refs(me_summary, known_classes))
    cls_name = method.get("name", "")
    refs.discard(cls_name)

    if me_key_methods:
        lines.append("**See also:** ")
        see_links = [f"[[#{km}|{km}]]" for km in me_key_methods if km != name]
        lines.append(", ".join(see_links))
        lines.append("\n")

    if refs:
        all_refs.update(refs)

    lines.append("---\n")


# ---------------------------------------------------------------------------
# Index and llms.txt renderers
# ---------------------------------------------------------------------------

def _render_index_page(
    class_list: list[str],
    enum_files: list[str],
    tutorial_files: list[str],
) -> str:
    """Render wiki/index.md with global navigation."""
    lines = [
        "---",
        "title: Index",
        "description: Global navigation for the Isaac Modding API wiki",
        "---",
        "",
        "# Isaac Modding API Wiki\n",
        "## Classes\n",
    ]
    for cls in sorted(class_list):
        lines.append(f"- [[classes/{cls}|{cls}]]")

    if enum_files:
        lines.append("\n## Enums\n")
        for ef in sorted(enum_files):
            name = Path(ef).stem
            lines.append(f"- [[enums/{name}|{name}]]")

    if tutorial_files:
        lines.append("\n## Tutorials\n")
        for tf in sorted(tutorial_files):
            name = Path(tf).stem
            lines.append(f"- [[tutorials/{name}|{name}]]")

    return "\n".join(lines) + "\n"


def _render_llms_txt(
    class_list: list[str],
    class_pages: dict[str, str],
    enum_files: list[str],
    tutorial_files: list[str],
) -> str:
    """Render wiki/llms.txt following llmstxt.org conventions."""
    lines = [
        "# Isaac Modding API Wiki",
        f"> {len(class_list)} classes, {len(enum_files)} enums, {len(tutorial_files)} tutorials",
        "",
        "## Classes\n",
    ]
    for cls in sorted(class_list):
        page = class_pages.get(cls, "")
        summary = ""
        m = re.search(r"## Summary\s*\n+(.+?)(?:\n##|\n#|\Z)", page, re.DOTALL)
        if m:
            summary = m.group(1).strip()
        lines.append(f"- **{cls}**: {summary}")

    if enum_files:
        lines.append("\n## Enums\n")
        for ef in sorted(enum_files):
            name = Path(ef).stem
            lines.append(f"- {name}")

    if tutorial_files:
        lines.append("\n## Tutorials\n")
        for tf in sorted(tutorial_files):
            name = Path(tf).stem
            lines.append(f"- {name}")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# WikiBuilder
# ---------------------------------------------------------------------------

class WikiBuilder:
    """Converts Isaac API data JSON into structured wiki markdown pages.

    Primary data source: ``processed_apis.json`` (72 class-organized entries
    with deduplicated class-level enhancements).

    Secondary source: ``rag_knowledge_base.json`` (per-method versions,
    modifiers, libraries).
    """

    def __init__(
        self,
        processed_apis_path: str | Path | None = None,
        kb_path: str | Path | None = None,
        raw_docs_dir: str | Path | None = None,
        wiki_dir: str | Path | None = None,
    ):
        root_dir = Path(__file__).resolve().parent.parent.parent
        data_dir = root_dir / "data"

        if processed_apis_path is None:
            processed_apis_path = data_dir / "processed_apis.json"
        if kb_path is None:
            kb_path = data_dir / "rag_knowledge_base.json"
        if raw_docs_dir is None:
            raw_docs_dir = root_dir / "Isaac-API" / "docs"
        if wiki_dir is None:
            wiki_dir = root_dir / "wiki"

        self.processed_apis_path = Path(processed_apis_path)
        self.kb_path = Path(kb_path)
        self.raw_docs_dir = Path(raw_docs_dir)
        self.wiki_dir = Path(wiki_dir)

    # ------------------------------------------------------------------
    # Main entry
    # ------------------------------------------------------------------
    def build_all(self) -> dict[str, Any]:
        """Build the complete wiki directory tree. Returns stats dict."""
        apis = self._load_json(self.processed_apis_path)
        kb = self._load_json(self.kb_path)

        known_classes = self._build_class_set(apis)
        versions_map, modifiers_map = self._build_kb_maps(kb)

        classes_dir = self.wiki_dir / "classes"
        enums_dir = self.wiki_dir / "enums"
        tutorials_dir = self.wiki_dir / "tutorials"
        for d in [classes_dir, enums_dir, tutorials_dir]:
            d.mkdir(parents=True, exist_ok=True)

        class_pages: dict[str, str] = {}
        class_names: list[str] = []
        total_methods = 0

        for entry in apis:
            class_name = entry.get("title", "")
            if not class_name:
                continue

            class_names.append(class_name)
            methods = entry.get("methods", [])
            class_enhancement = entry.get("enhancement", {})
            method_enhancements = entry.get("method_enhancements", {})

            page = _render_class_page(
                class_name=class_name,
                methods=methods,
                class_enhancement=class_enhancement,
                method_enhancements=method_enhancements,
                known_classes=known_classes,
                versions_map=versions_map,
                modifiers_map=modifiers_map,
            )

            class_pages[class_name] = page
            total_methods += len(methods)

            out_path = classes_dir / f"{class_name}.md"
            out_path.write_text(page, encoding="utf-8")

        enum_files = self._copy_enums(enums_dir)
        tutorial_files = self._copy_tutorials(tutorials_dir)

        index_md = _render_index_page(class_names, enum_files, tutorial_files)
        (self.wiki_dir / "index.md").write_text(index_md, encoding="utf-8")

        llms_txt = _render_llms_txt(class_names, class_pages, enum_files, tutorial_files)
        (self.wiki_dir / "llms.txt").write_text(llms_txt, encoding="utf-8")

        stats = {
            "classes": len(class_names),
            "total_methods": total_methods,
            "enums": len(enum_files),
            "tutorials": len(tutorial_files),
            "wiki_dir": str(self.wiki_dir),
            "avg_methods_per_class": round(total_methods / max(len(class_names), 1), 1),
        }
        return stats

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _load_json(self, path: Path) -> Any:
        if not path.exists():
            raise FileNotFoundError(f"Data file not found: {path}")
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)

    def _build_class_set(self, apis: list[dict]) -> set[str]:
        names: set[str] = set()
        for entry in apis:
            title = entry.get("title", "")
            if title:
                names.add(title)
        return names

    def _build_kb_maps(
        self, kb: list[dict],
    ) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
        versions_map: dict[str, list[str]] = defaultdict(list)
        modifiers_map: dict[str, list[str]] = defaultdict(list)

        for entry in kb:
            mid = entry.get("method_id", "")
            if mid:
                versions = entry.get("versions", [])
                modifiers = entry.get("modifiers", [])
                if versions:
                    versions_map[mid] = versions
                if modifiers:
                    modifiers_map[mid] = modifiers

        return dict(versions_map), dict(modifiers_map)

    def _copy_enums(self, enums_dir: Path) -> list[str]:
        src = self.raw_docs_dir / "enums"
        if not src.exists():
            return []

        copied: list[str] = []
        for md_file in sorted(src.glob("*.md")):
            content = md_file.read_text(encoding="utf-8")
            content = re.sub(r"\{:\s*\.[^}]+\}", "", content)
            content = re.sub(r"--8<--\s*\"[^\"]*\"", "", content)

            dest = enums_dir / md_file.name
            dest.write_text(content, encoding="utf-8")
            copied.append(md_file.name)

        return copied

    def _copy_tutorials(self, tutorials_dir: Path) -> list[str]:
        src = self.raw_docs_dir / "tutorials"
        if not src.exists():
            return []

        copied: list[str] = []
        for md_file in sorted(src.glob("*.md")):
            if md_file.stat().st_size > 100_000:
                continue
            content = md_file.read_text(encoding="utf-8")
            content = re.sub(r"\{:\s*\.[^}]+\}", "", content)

            dest = tutorials_dir / md_file.name
            dest.write_text(content, encoding="utf-8")
            copied.append(md_file.name)

        return copied


# ---------------------------------------------------------------------------
# CLI entry for standalone use
# ---------------------------------------------------------------------------
def main() -> None:
    """Build the wiki from the command line."""
    builder = WikiBuilder()
    print(f"Building wiki from:")
    print(f"  APIs: {builder.processed_apis_path}")
    print(f"  KB:   {builder.kb_path}")
    print(f"  Raw:  {builder.raw_docs_dir}")
    print(f"  Out:  {builder.wiki_dir}")
    print()

    stats = builder.build_all()

    print("Wiki built successfully!")
    print(f"  Classes:   {stats['classes']}")
    print(f"  Methods:   {stats['total_methods']}")
    print(f"  Enums:     {stats['enums']}")
    print(f"  Tutorials: {stats['tutorials']}")
    print(f"  Avg methods/class: {stats['avg_methods_per_class']}")
    print(f"  Output:    {stats['wiki_dir']}")


if __name__ == "__main__":
    main()
