"""Tests for validated bilingual catalog persistence."""

import json
from pathlib import Path

from isaac_wiki.catalog_store import CatalogStore


def _entry(*, origin: str = "upstream", inference_basis: str | None = None) -> dict:
    description = {
        "en": {"text": "Adds a knockback effect.", "origin": origin},
        "zh": {"text": "添加击退效果。", "origin": origin},
    }
    if inference_basis:
        description["en"]["inference_basis"] = inference_basis
        description["zh"]["inference_basis"] = inference_basis
    return {
        "id": "entity.add_knockback",
        "title": "Entity:AddKnockback",
        "kind": "method",
        "variants": [
            {
                "id": "entity.add_knockback",
                "relation": "base",
                "games": ["rep", "rep+"],
                "dependencies": [],
                "signature": "Entity:AddKnockback(entity, force)",
                "source": {
                    "repository_url": "https://github.com/3113y/isaac-api-edition",
                    "revision": "3bcfd953aea381f9fdd1fd0767f7d9317f8ac02e",
                    "source_path": "docs/en/Entity.md",
                },
                "description": description,
            }
        ],
    }


def _write_entry(directory: Path, **kwargs: object) -> None:
    (directory / "entity.add_knockback.json").write_text(
        json.dumps(_entry(**kwargs), ensure_ascii=False), encoding="utf-8"
    )


def test_store_reads_a_bilingual_entry(tmp_path: Path) -> None:
    _write_entry(tmp_path)

    store = CatalogStore(tmp_path)

    assert store.validate() == []
    assert store.entries()[0].variants[0].description("zh").text == "添加击退效果。"


def test_store_rejects_inferred_text_without_an_inference_basis(tmp_path: Path) -> None:
    _write_entry(tmp_path, origin="inferred")

    assert "inference_basis is required for inferred text" in CatalogStore(tmp_path).validate()[0]


def test_store_rejects_missing_source_revision(tmp_path: Path) -> None:
    payload = _entry()
    payload["variants"][0]["source"]["revision"] = ""
    (tmp_path / "broken.json").write_text(json.dumps(payload), encoding="utf-8")

    assert "source revision is required" in CatalogStore(tmp_path).validate()[0]
