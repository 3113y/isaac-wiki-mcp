"""Tests for WikiEngine — full-text search and page retrieval."""

from pathlib import Path

import pytest

from isaac_wiki.wiki_engine import (
    WikiEngine,
    _cjk_ratio,
    _default_wiki_dir,
    _parse_frontmatter,
    _tokenize,
)


def test_test_suite_is_tracked() -> None:
    assert Path(__file__).exists()


def test_default_wiki_dir_prefers_bundled_package_data(tmp_path: Path) -> None:
    package_file = tmp_path / "site-packages" / "isaac_wiki" / "wiki_engine.py"
    package_file.parent.mkdir(parents=True)
    package_file.touch()
    bundled_wiki = package_file.parent / "wiki"
    bundled_wiki.mkdir()

    assert _default_wiki_dir(package_file) == bundled_wiki


class TestTokenization:
    def test_english_tokens(self) -> None:
        tokens = _tokenize("add hearts player")
        assert {"add", "hearts", "player"} <= set(tokens)

    def test_cjk_detection(self) -> None:
        assert _cjk_ratio("添加黑心") > 0.5
        assert _cjk_ratio("hello world") < 0.1

    def test_cjk_bigram_tokens(self) -> None:
        assert any(len(token) == 2 for token in _tokenize("添加黑心"))

    def test_mixed_tokens(self) -> None:
        assert "addhearts" in _tokenize("AddHearts 添加")


def test_parse_frontmatter() -> None:
    content = """---
title: EntityPlayer
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 276
---

# EntityPlayer
"""
    meta = _parse_frontmatter(content)
    assert meta == {
        "title": "EntityPlayer",
        "category": "class",
        "dlc_versions": ["AB+", "REP", "REP+"],
        "method_count": 276,
    }


@pytest.fixture(scope="module")
def engine() -> WikiEngine:
    return WikiEngine(wiki_dir=Path(__file__).resolve().parent.parent / "wiki")


class TestWikiEngine:
    def test_stats(self, engine: WikiEngine) -> None:
        stats = engine.get_stats()
        assert stats["total_pages"] > 0
        assert stats["classes"] > 0
        assert stats["total_methods"] > 0

    def test_read_page_by_name(self, engine: WikiEngine) -> None:
        page = engine.read_page("EntityPlayer")
        assert page is not None
        assert page["title"] == "EntityPlayer"
        assert "Inherits from:" in page["content"]

    def test_search_english(self, engine: WikiEngine) -> None:
        assert any("EntityPlayer" in item["title"] for item in engine.search("add hearts", top_k=3))

    def test_search_chinese(self, engine: WikiEngine) -> None:
        assert engine.search("玩家生命值", top_k=3)

    def test_search_with_category(self, engine: WikiEngine) -> None:
        results = engine.search("spawn", category="classes", top_k=3)
        assert results
        assert all(item["path"].startswith("classes/") for item in results)
