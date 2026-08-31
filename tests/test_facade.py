"""Tests for WikiFacade — JSON-safe wrapper around WikiEngine."""

from pathlib import Path

import pytest

from isaac_wiki.facade import WikiFacade


@pytest.fixture(scope="module")
def facade() -> WikiFacade:
    """Provide a WikiFacade pointed at the project wiki directory."""
    wiki_dir = Path(__file__).resolve().parent.parent / "wiki"
    if not wiki_dir.exists():
        pytest.skip("wiki/ directory not built — run wiki_builder first")
    return WikiFacade(wiki_dir=str(wiki_dir))


def test_test_suite_is_tracked() -> None:
    assert Path(__file__).exists()


class TestWikiFacade:
    def test_search_returns_ok(self, facade: WikiFacade) -> None:
        result = facade.search("player health", top_k=3)
        assert result["status"] == "ok"
        assert result["total_results"] > 0
        assert len(result["results"]) <= 3
        assert all("content" in item for item in result["results"])

    def test_search_with_category(self, facade: WikiFacade) -> None:
        result = facade.search("spawn", category="classes", top_k=3)
        assert result["status"] == "ok"
        assert all(item["path"].startswith("classes/") for item in result["results"])

    def test_read_page(self, facade: WikiFacade) -> None:
        result = facade.read_page("EntityPlayer")
        assert result["status"] == "ok"
        assert result["title"] == "EntityPlayer"
        assert "AddBlackHearts" in result["content"]

    def test_read_page_not_found(self, facade: WikiFacade) -> None:
        assert facade.read_page("NonExistentClass")["status"] == "error"

    def test_list_pages(self, facade: WikiFacade) -> None:
        result = facade.list_pages("classes")
        assert result["status"] == "ok"
        assert result["count"] > 0
        assert all(item["category"] == "classes" for item in result["pages"])

    def test_stats(self, facade: WikiFacade) -> None:
        result = facade.stats()
        assert result["status"] == "ok"
        assert result["total_pages"] > 0

    def test_categories(self, facade: WikiFacade) -> None:
        result = facade.categories()
        assert result["status"] == "ok"
        assert "classes" in result["categories"]
