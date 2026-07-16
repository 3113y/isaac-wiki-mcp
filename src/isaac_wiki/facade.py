"""
WikiFacade — unified public API with JSON-safe returns.

All methods return plain dicts (never raise), making the facade safe
for direct use in MCP tools, CLI commands, and third-party scripts.

Provides full-text search, page reading, and category browsing over
the wiki/ directory, with zero ML dependencies.
"""

from __future__ import annotations

import time
from typing import Any

from loguru import logger


class WikiFacade:
    """Entry point for MCP server and CLI.

    Wraps :class:`WikiEngine` so every public method returns a
    ``{"status": "ok", ...}`` or ``{"status": "error", "error": "..."}``
    dict — callers never need a try/except.
    """

    def __init__(self, wiki_dir: str | None = None):
        self._engine = None  # type: ignore[assignment]
        self._wiki_dir = wiki_dir

    def _get_engine(self):
        if self._engine is None:
            from isaac_wiki.wiki_engine import WikiEngine
            self._engine = WikiEngine(wiki_dir=self._wiki_dir)
        return self._engine

    @staticmethod
    def _ok(data: dict[str, Any] | None = None) -> dict[str, Any]:
        d = dict(data) if data else {}
        d.setdefault("status", "ok")
        return d

    @staticmethod
    def _err(msg: str) -> dict[str, Any]:
        logger.error(msg)
        return {"status": "error", "error": msg}

    # ------------------------------------------------------------------
    def search(
        self,
        query: str,
        top_k: int = 5,
        category: str | None = None,
    ) -> dict[str, Any]:
        t0 = time.perf_counter()
        try:
            engine = self._get_engine()
            results = engine.search(query, top_k, category=category)
            elapsed = (time.perf_counter() - t0) * 1000
            return self._ok({
                "query": query,
                "results": results,
                "total_results": len(results),
                "search_time_ms": round(elapsed, 3),
            })
        except Exception as exc:
            return self._err(str(exc))

    def read_page(self, page: str) -> dict[str, Any]:
        try:
            engine = self._get_engine()
            result = engine.read_page(page)
            if result is None:
                return self._err(f"Page not found: {page}")
            return self._ok(result)
        except Exception as exc:
            return self._err(str(exc))

    def list_pages(self, category: str | None = None) -> dict[str, Any]:
        try:
            engine = self._get_engine()
            pages = engine.list_pages(category)
            return self._ok({"pages": pages, "count": len(pages)})
        except Exception as exc:
            return self._err(str(exc))

    def stats(self) -> dict[str, Any]:
        try:
            return self._ok(self._get_engine().get_stats())
        except Exception as exc:
            return self._err(str(exc))

    def categories(self) -> dict[str, Any]:
        try:
            cats = self._get_engine().list_categories()
            return self._ok({"categories": cats, "count": len(cats)})
        except Exception as exc:
            return self._err(str(exc))
