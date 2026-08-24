"""Query and render structured bilingual API catalog entries."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from isaac_wiki.catalog import EnvironmentProfile, resolve_variants
from isaac_wiki.catalog_store import CatalogStore, CatalogVariant, Description


INFERRED_NOTICE = {
    "zh": "LLM 智能推断说明：上游文档未提供此描述。",
    "en": "LLM-inferred description: no upstream description was provided.",
}


def _language_for(value: str, query: str = "") -> str:
    if value not in {"auto", "zh", "en"}:
        raise ValueError("language must be auto, zh, or en")
    if value == "auto":
        return "zh" if re.search(r"[\u4e00-\u9fff]", query) else "en"
    return value


def render_description(description: Description, language: str) -> str:
    if description.origin != "inferred":
        return description.text
    return f"{description.text}\n\n{INFERRED_NOTICE[language]}"


class CatalogEngine:
    """Searches catalog data after resolving a caller's mod environment."""

    def __init__(self, catalog_dir: str | Path | None = None):
        if catalog_dir is None:
            development = Path(__file__).resolve().parents[2] / "data" / "catalog"
            packaged = Path(__file__).resolve().parent / "data" / "catalog"
            catalog_dir = development if development.exists() else packaged
        self.store = CatalogStore(catalog_dir)

    def _records(
        self,
        profile: EnvironmentProfile,
        language: str,
        *,
        query: str = "",
        include_incompatible: bool = False,
    ) -> list[dict[str, Any]]:
        errors = self.store.validate()
        if errors:
            raise ValueError("invalid catalog: " + "; ".join(errors))
        selected_language = _language_for(language, query)
        records: list[tuple[Any, CatalogVariant, bool]] = []
        for entry in self.store.entries():
            variants = list(entry.variants)
            if include_incompatible:
                active_ids = {
                    item.id
                    for item in resolve_variants(
                        [item.to_api_variant() for item in variants], profile
                    )
                }
                chosen = variants
            else:
                active = resolve_variants(
                    [item.to_api_variant() for item in variants], profile
                )
                active_ids = {item.id for item in active}
                chosen = [item for item in variants if item.id in active_ids]
            records.extend(
                (entry, variant, variant.id in active_ids) for variant in chosen
            )
        return [
            self._render(entry, variant, compatible, selected_language)
            for entry, variant, compatible in records
        ]

    @staticmethod
    def _render(
        entry: Any, variant: CatalogVariant, compatible: bool, language: str
    ) -> dict[str, Any]:
        description = variant.description(language)
        content = render_description(description, language)
        return {
            "id": variant.id,
            "entry_id": entry.id,
            "title": entry.id,
            "kind": entry.kind,
            "signature": variant.signature,
            "content": content,
            "description": content,
            "language": language,
            "description_origin": description.origin,
            "compatible": compatible,
            "environment": {
                "game": variant.game,
                "dependencies": list(variant.dependencies),
            },
            "relation": variant.relation,
            "overrides": variant.overrides,
            "source": {
                "repository_url": variant.source.repository_url,
                "revision": variant.source.revision,
                "source_path": variant.source.source_path,
            },
        }

    def search(
        self,
        query: str,
        profile: EnvironmentProfile,
        language: str = "auto",
        include_incompatible: bool = False,
    ) -> list[dict[str, Any]]:
        needle = query.casefold().strip()
        records = self._records(
            profile, language, query=query, include_incompatible=include_incompatible
        )
        if not needle:
            return records
        return [
            record
            for record in records
            if needle
            in " ".join(
                [record["id"], record["title"], record["signature"], record["content"]]
            ).casefold()
        ]

    def read(
        self,
        page: str,
        profile: EnvironmentProfile,
        language: str = "auto",
        include_incompatible: bool = False,
    ) -> dict[str, Any] | None:
        for record in self._records(
            profile, language, query=page, include_incompatible=include_incompatible
        ):
            if page in {record["id"], record["entry_id"], record["title"]}:
                return record
        return None

    def list(
        self,
        profile: EnvironmentProfile,
        language: str = "auto",
        include_incompatible: bool = False,
    ) -> list[dict[str, Any]]:
        return self._records(
            profile, language, include_incompatible=include_incompatible
        )
