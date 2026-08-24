import json

from isaac_wiki.catalog import EnvironmentProfile
from isaac_wiki.catalog_engine import CatalogEngine
from isaac_wiki.facade import WikiFacade


def _write_entry(directory, *, entry_id="UndocumentedMethod", dependency=None, origin="inferred"):
    dependencies = [dependency] if dependency else []
    payload = {
        "id": entry_id,
        "kind": "method",
        "signature": "EntityPlayer:UndocumentedMethod()",
        "variants": [
            {
                "id": entry_id,
                "relation": "base" if not dependency else "extension",
                "environment": {"game": "rep", "dependencies": dependencies},
                "signature": "EntityPlayer:UndocumentedMethod()",
                "source": {
                    "repository_url": "https://example.invalid/source",
                    "revision": "test",
                    "source_path": "api.md",
                },
                "descriptions": {
                    "en": {
                        "text": "A generated description.",
                        "origin": origin,
                        "inference_basis": "method name" if origin == "inferred" else None,
                    },
                    "zh": {
                        "text": "智能推断的描述。",
                        "origin": origin,
                        "inference_basis": "方法名" if origin == "inferred" else None,
                    },
                },
            }
        ],
    }
    (directory / f"{entry_id}.json").write_text(
        json.dumps(payload, ensure_ascii=False), encoding="utf-8"
    )


def test_chinese_inferred_text_ends_with_required_notice(tmp_path):
    _write_entry(tmp_path)
    facade = WikiFacade(catalog_dir=tmp_path, wiki_dir=tmp_path / "missing-wiki")

    result = facade.read_page(
        "UndocumentedMethod", game="rep", dependencies=[], language="zh"
    )

    assert result["status"] == "ok"
    assert result["content"].endswith("LLM 智能推断说明：上游文档未提供此描述。")


def test_rgon_override_replaces_base_and_eid_is_profile_gated(tmp_path):
    base = {
        "id": "player.add_hearts",
        "kind": "method",
        "signature": "EntityPlayer:AddHearts(amount)",
        "variants": [
            {
                "id": "player.add_hearts",
                "relation": "base",
                "environment": {"game": "rep", "dependencies": []},
                "signature": "EntityPlayer:AddHearts(amount)",
                "source": {"repository_url": "https://example.invalid/rep", "revision": "r", "source_path": "api.md"},
                "descriptions": {"en": {"text": "Base hearts.", "origin": "upstream"}, "zh": {"text": "基础心之容器。", "origin": "translated"}},
            },
            {
                "id": "rgon.player.add_hearts",
                "relation": "override",
                "overrides": "player.add_hearts",
                "environment": {"game": "rep", "dependencies": ["rgon"]},
                "signature": "EntityPlayer:AddHearts(amount)",
                "source": {"repository_url": "https://example.invalid/rgon", "revision": "r", "source_path": "api.md"},
                "descriptions": {"en": {"text": "RGON hearts.", "origin": "upstream"}, "zh": {"text": "RGON 心之容器。", "origin": "translated"}},
            },
        ],
    }
    (tmp_path / "base.json").write_text(json.dumps(base, ensure_ascii=False), encoding="utf-8")
    _write_entry(tmp_path, entry_id="eid.item.description", dependency="eid", origin="upstream")
    engine = CatalogEngine(tmp_path)

    rgon = engine.search("hearts", EnvironmentProfile.from_values("rep", ["rgon"]), "en")
    assert [item["id"] for item in rgon] == ["rgon.player.add_hearts"]
    assert engine.search("description", EnvironmentProfile.from_values("rep", []), "en") == []
    assert engine.search("description", EnvironmentProfile.from_values("rep", ["eid"]), "en")


def test_include_incompatible_marks_unavailable_variants(tmp_path):
    _write_entry(tmp_path, entry_id="rep_plus_only", dependency=None)
    engine = CatalogEngine(tmp_path)
    profile = EnvironmentProfile.from_values("rep+", [])

    results = engine.search("generated", profile, "en", include_incompatible=True)

    assert results[0]["compatible"] is False

