"""Tests for WikiFacade — JSON-safe wrapper around WikiEngine."""

import tempfile
from pathlib import Path

import pytest

from isaac_wiki.facade import WikiFacade
from isaac_wiki.wiki_engine import WikiEngine


@pytest.fixture(scope="module")
def facade():
    """Provide a WikiFacade pointed at the project wiki directory."""
    wiki_dir = Path(__file__).resolve().parent.parent / "wiki"
    if not wiki_dir.exists():
        pytest.skip("wiki/ directory not built — run wiki_builder first")
    return WikiFacade(wiki_dir=str(wiki_dir))


class TestWikiFacade:
    def test_search_returns_ok(self, facade):
        result = facade.search("player health", top_k=3)
        assert result["status"] == "ok"
        assert result["total_results"] > 0
        assert len(result["results"]) <= 3
        # Each result should have content (full page, not chunk)
        for r in result["results"]:
            assert "content" in r
            assert "title" in r
            assert "path" in r

    def test_search_with_category(self, facade):
        result = facade.search("spawn", category="classes", top_k=3)
        assert result["status"] == "ok"
        for r in result["results"]:
            assert r["path"].startswith("classes/")

    def test_read_page(self, facade):
        result = facade.read_page("EntityPlayer")
        assert result["status"] == "ok"
        assert result["title"] == "EntityPlayer"
        assert result["category"] == "classes"
        assert "AddBlackHearts" in result["content"]

    def test_read_page_not_found(self, facade):
        result = facade.read_page("NonExistentClass")
        assert result["status"] == "error"

    def test_list_pages(self, facade):
        result = facade.list_pages("classes")
        assert result["status"] == "ok"
        assert result["count"] > 0
        for p in result["pages"]:
            assert p["category"] == "classes"

    def test_stats(self, facade):
        result = facade.stats()
        assert result["status"] == "ok"
        assert result["total_pages"] > 0
        assert result["classes"] > 0

    def test_categories(self, facade):
        result = facade.categories()
        assert result["status"] == "ok"
        assert "classes" in result["categories"]

    def test_error_handling_empty_query(self, facade):
        result = facade.search("")
        # Empty query should still return ok (no tokens match = no results)
        assert "status" in result
