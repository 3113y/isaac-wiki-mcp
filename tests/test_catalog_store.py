import json

import pytest

from isaac_wiki.catalog_store import CatalogStore


SOURCE_URL = "https://github.com/wofsauge/External-Item-Descriptions"


def write_entry(tmp_path, *, source=SOURCE_URL, dependency="eid", **changes):
    variant = {
        "id": "eid.item.add_description",
        "relation": "extension",
        "environment": {"game": "rep", "dependencies": [dependency]},
        "signature": "EID:AddItemDescription(id, description)",
        "source": {
            "repository_url": source,
            "revision": "0123456789abcdef",
            "source_path": "docs/api.md",
        },
        "descriptions": {
            "en": {"text": "Adds an item description.", "origin": "upstream"},
            "zh": {"text": "添加道具说明。", "origin": "translated"},
        },
    }
    entry = {
        "id": "eid.item.add_description",
        "kind": "method",
        "signature": "EID:AddItemDescription(id, description)",
        "variants": [variant],
    }
    for key, value in changes.items():
        if key == "variant":
            entry["variants"][0].update(value)
        else:
            entry[key] = value
    (tmp_path / "entry.json").write_text(
        json.dumps(entry, ensure_ascii=False), encoding="utf-8"
    )


def test_store_reads_a_bilingual_eid_entry(tmp_path):
    write_entry(tmp_path)
    store = CatalogStore(tmp_path)

    assert store.validate() == []
    assert store.entries()[0].variants[0].description("zh").text == "添加道具说明。"


def test_store_rejects_missing_source_revision(tmp_path):
    write_entry(tmp_path, variant={"source": {"repository_url": SOURCE_URL, "source_path": "docs/api.md"}})

    assert any("revision" in error for error in CatalogStore(tmp_path).validate())


def test_store_rejects_missing_chinese_translation(tmp_path):
    write_entry(tmp_path, variant={"descriptions": {"en": {"text": "Adds it.", "origin": "upstream"}}})

    assert any("zh" in error for error in CatalogStore(tmp_path).validate())


def test_store_rejects_inferred_text_without_basis(tmp_path):
    write_entry(
        tmp_path,
        variant={
            "descriptions": {
                "en": {"text": "Adds it.", "origin": "inferred"},
                "zh": {"text": "添加它。", "origin": "inferred"},
            }
        },
    )

    assert sum("inference_basis" in error for error in CatalogStore(tmp_path).validate()) == 2


def test_store_rejects_unresolved_override(tmp_path):
    write_entry(
        tmp_path,
        variant={"relation": "override", "overrides": "missing.base.member"},
    )

    assert any("overrides" in error and "missing.base.member" in error for error in CatalogStore(tmp_path).validate())


@pytest.mark.parametrize("payload", [[], {"variants": [None]}, {"variants": {"bad": "shape"}}])
def test_store_reports_malformed_json_shapes_without_raising(tmp_path, payload):
    (tmp_path / "entry.json").write_text(json.dumps(payload), encoding="utf-8")

    errors = CatalogStore(tmp_path).validate()

    assert errors
