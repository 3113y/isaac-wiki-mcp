"""Tests for WikiEngine — full-text search and page retrieval."""

import tempfile
from pathlib import Path

import pytest

from isaac_wiki.wiki_engine import WikiEngine, _tokenize, _cjk_ratio, _parse_frontmatter


# ---------------------------------------------------------------------------
# Tokenization tests
# ---------------------------------------------------------------------------
class TestTokenization:
    def test_english_tokens(self):
        tokens = _tokenize("add hearts player")
        assert "add" in tokens
        assert "hearts" in tokens
        assert "player" in tokens

    def test_cjk_detection(self):
        assert _cjk_ratio("添加黑心") > 0.5
        assert _cjk_ratio("hello world") < 0.1

    def test_cjk_bigram_tokens(self):
        tokens = _tokenize("添加黑心")
        # Should produce bigrams like "添加", "加黑", "黑心"
        assert any(len(t) == 2 for t in tokens)

    def test_mixed_tokens(self):
        tokens = _tokenize("AddHearts 添加")
        assert "addhearts" in tokens


# ---------------------------------------------------------------------------
# Frontmatter parsing tests
# ---------------------------------------------------------------------------
class TestFrontmatter:
    def test_parse_frontmatter(self):
        content = """---
title: EntityPlayer
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 276
---

# EntityPlayer
"""
        meta = _parse_frontmatter(content)
        assert meta["title"] == "EntityPlayer"
        assert meta["category"] == "class"
        assert meta["dlc_versions"] == ["AB+", "REP", "REP+"]
        assert meta["method_count"] == 276

    def test_no_frontmatter(self):
        meta = _parse_frontmatter("# Just a heading\n\nSome content.")
        assert meta == {}


# ---------------------------------------------------------------------------
# WikiEngine tests (against real wiki data)
# ---------------------------------------------------------------------------
@pytest.fixture(scope="module")
def engine():
    """Provide a WikiEngine pointed at the project wiki directory."""
    wiki_dir = Path(__file__).resolve().parent.parent / "wiki"
    if not wiki_dir.exists():
        pytest.skip("wiki/ directory not built — run wiki_builder first")
    return WikiEngine(wiki_dir=wiki_dir)


class TestWikiEngine:
    def test_stats(self, engine):
        stats = engine.get_stats()
        assert stats["total_pages"] > 0
        assert stats["classes"] > 0
        assert stats["total_methods"] > 0

    def test_list_categories(self, engine):
        cats = engine.list_categories()
        assert "classes" in cats
        assert "enums" in cats

    def test_read_page_by_name(self, engine):
        page = engine.read_page("EntityPlayer")
        assert page is not None
        assert page["title"] == "EntityPlayer"
        assert page["category"] == "classes"
        assert len(page["content"]) > 1000
        assert "Inherits from:" in page["content"]

    def test_read_page_by_path(self, engine):
        page = engine.read_page("classes/EntityPlayer.md")
        assert page is not None
        assert page["title"] == "EntityPlayer"

    def test_read_page_not_found(self, engine):
        page = engine.read_page("NonExistentClass")
        assert page is None

    def test_search_english(self, engine):
        results = engine.search("add hearts", top_k=3)
        assert len(results) > 0
        # EntityPlayer should be top result
        assert any("EntityPlayer" in r["title"] for r in results)

    def test_search_chinese(self, engine):
        results = engine.search("玩家生命值", top_k=3)
        assert len(results) > 0

    def test_search_with_category(self, engine):
        results = engine.search("spawn", category="classes", top_k=3)
        assert len(results) > 0
        for r in results:
            assert r["path"].startswith("classes/")

    def test_list_pages_all(self, engine):
        pages = engine.list_pages()
        assert len(pages) > 0
        # Each page should have required fields
        for p in pages[:5]:
            assert "path" in p
            assert "title" in p
            assert "category" in p

    def test_list_pages_filtered(self, engine):
        pages = engine.list_pages(category="classes")
        assert len(pages) > 0
        for p in pages:
            assert p["category"] == "classes"

    def test_content_has_wikilinks(self, engine):
        page = engine.read_page("EntityPlayer")
        assert page is not None
        assert "Inherits from: [[Entity]]" in page["content"]
        assert "[[Vector]]" in page["content"]
