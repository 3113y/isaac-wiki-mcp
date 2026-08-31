"""Tests for profile-aware access to the bundled API Edition snapshot."""

import re
from pathlib import Path

from isaac_wiki.facade import WikiFacade


def _write_reference(root: Path) -> None:
    page = """# Entity

## AddKnockback

Applies knockback.

<div class=\"rgon-extension\" markdown=\"1\">

## AddKnockback

RGON adds a direction argument.

</div>
"""
    for language in ("en", "zh"):
        directory = root / "reference" / language
        directory.mkdir(parents=True)
        (directory / "Entity.md").write_text(page, encoding="utf-8")


def test_profile_search_uses_the_requested_language_and_hides_rgon_by_default(tmp_path: Path) -> None:
    _write_reference(tmp_path)
    facade = WikiFacade(wiki_dir=str(tmp_path))

    result = facade.search("knockback", game="rep", language="en")

    assert result["status"] == "ok"
    assert result["results"][0]["path"] == "reference/en/Entity.md"
    assert "RGON adds" not in result["results"][0]["content"]
    assert result["profile"] == {"game": "rep", "dependencies": [], "language": "en"}


def test_profile_read_keeps_rgon_extensions_when_enabled(tmp_path: Path) -> None:
    _write_reference(tmp_path)
    facade = WikiFacade(wiki_dir=str(tmp_path))

    result = facade.read_page("Entity", game="rep+", dependencies=["rgon"], language="zh")

    assert result["status"] == "ok"
    assert result["path"] == "reference/zh/Entity.md"
    assert "RGON adds a direction argument." in result["content"]
    assert result["profile"] == {"game": "rep+", "dependencies": ["rgon"], "language": "zh"}


def test_sources_reports_the_bundled_snapshot_revision(tmp_path: Path) -> None:
    source_dir = tmp_path / "reference"
    source_dir.mkdir()
    (source_dir / "source-release.json").write_text(
        '{"repository":"https://github.com/3113y/isaac-api-edition","snapshot_revision":"abc123"}',
        encoding="utf-8",
    )

    result = WikiFacade(wiki_dir=str(tmp_path)).sources()

    assert result["status"] == "ok"
    assert result["snapshot"]["snapshot_revision"] == "abc123"


def test_bundled_snapshot_contains_both_languages_and_the_source_manifest() -> None:
    root = Path(__file__).resolve().parent.parent / "wiki" / "reference"
    manifest = (root / "source-release.json").read_text(encoding="utf-8")

    assert (root / "en" / "Entity.md").exists()
    assert (root / "zh" / "Entity.md").exists()
    assert '"repository": "https://github.com/3113y/isaac-api-edition"' in manifest
    assert re.search(r'"snapshot_revision": "[0-9a-f]{40}"', manifest)


def test_bundled_snapshot_contains_only_queryable_markdown() -> None:
    root = Path(__file__).resolve().parent.parent / "wiki" / "reference"
    unexpected = [
        path for path in root.rglob("*")
        if path.is_file() and path.suffix not in {".md", ".json"}
    ]

    assert unexpected == []
