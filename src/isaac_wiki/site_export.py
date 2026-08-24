"""Export validated catalog records as paired Markdown pages for GitHub Pages."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from isaac_wiki.catalog_engine import render_description
from isaac_wiki.catalog_store import CatalogStore, CatalogVariant


def _class_name(signature: str) -> str:
    owner = signature.split(":", 1)[0].strip()
    return owner or "API"


def _source_url(variant: CatalogVariant) -> str:
    return (
        f"{variant.source.repository_url}/blob/{variant.source.revision}/"
        f"{variant.source.source_path}"
    )


def _render_variant(variant: CatalogVariant, language: str) -> str:
    dependencies = ", ".join(variant.dependencies) or "none"
    labels = (
        f"Game: {variant.game} | Dependencies: {dependencies} | "
        f"Relation: {variant.relation}"
    )
    override = f"\n\nOverrides: `{variant.overrides}`" if variant.overrides else ""
    return (
        f"```lua\n{variant.signature}\n```\n\n{labels}\n\n"
        f"{render_description(variant.description(language), language)}"
        f"{override}\n\nSource: [{variant.source.source_path}]({_source_url(variant)})"
    )


def export_site(catalog: CatalogStore, output_dir: Path, release: dict[str, Any]) -> None:
    errors = catalog.validate()
    if errors:
        raise ValueError("invalid catalog: " + "; ".join(errors))
    output_dir.mkdir(parents=True, exist_ok=True)
    pages: dict[str, list[CatalogVariant]] = defaultdict(list)
    for entry in catalog.entries():
        for variant in entry.variants:
            pages[_class_name(variant.signature)].append(variant)

    page_map: dict[str, str] = {}
    for owner, variants in sorted(pages.items()):
        for language in ("en", "zh"):
            relative = Path(language) / "classes" / f"{owner}.md"
            destination = output_dir / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            heading = owner if language == "en" else owner
            sections = "\n\n---\n\n".join(_render_variant(item, language) for item in variants)
            destination.write_text(f"# {heading}\n\n{sections}\n", encoding="utf-8")
        page_map[f"zh/classes/{owner}"] = f"en/classes/{owner}"
        page_map[f"en/classes/{owner}"] = f"zh/classes/{owner}"

    (output_dir / "release.json").write_text(
        json.dumps(release, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (output_dir / "page-map.json").write_text(
        json.dumps(page_map, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
