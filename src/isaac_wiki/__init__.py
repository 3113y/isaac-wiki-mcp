"""
isaac_wiki — Wiki system for Isaac modding API documentation.

Provides llmwiki-style full-text search over The Binding of Isaac:
Repentance modding API docs. Zero ML dependencies — pure Python
file-system-native markdown wiki.

Exports:
    - WikiFacade (JSON-safe public API)
    - WikiEngine (low-level search/page engine)
    - WikiBuilder (data → wiki markdown converter)
"""

from isaac_wiki.facade import WikiFacade
from isaac_wiki.wiki_engine import WikiEngine
from isaac_wiki.wiki_builder import WikiBuilder
from isaac_wiki.catalog_store import CatalogStore

__version__ = "0.2.0"
__all__ = ["CatalogStore", "WikiFacade", "WikiEngine", "WikiBuilder"]
