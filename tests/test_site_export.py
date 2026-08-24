import json

from isaac_wiki.catalog_store import CatalogStore
from isaac_wiki.site_export import export_site


def test_export_creates_paired_entity_player_pages(tmp_path):
    catalog_dir = tmp_path / "catalog"
    catalog_dir.mkdir()
    (catalog_dir / "entry.json").write_text(
        json.dumps(
            {
                "id": "player.add_hearts",
                "kind": "method",
                "signature": "EntityPlayer:AddHearts(amount)",
                "variants": [
                    {
                        "id": "player.add_hearts",
                        "relation": "base",
                        "environment": {"game": "rep", "dependencies": []},
                        "signature": "EntityPlayer:AddHearts(amount)",
                        "source": {"repository_url": "https://example.invalid/rep", "revision": "a" * 40, "source_path": "docs/EntityPlayer.md"},
                        "descriptions": {
                            "en": {"text": "Adds heart containers.", "origin": "upstream"},
                            "zh": {"text": "添加心之容器。", "origin": "inferred", "inference_basis": "signature"}
                        }
                    }
                ]
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    output = tmp_path / "site"

    export_site(CatalogStore(catalog_dir), output, {"catalog_revision": "test"})

    assert (output / "en" / "classes" / "EntityPlayer.md").exists()
    assert (output / "zh" / "classes" / "EntityPlayer.md").exists()
    page_map = json.loads((output / "page-map.json").read_text(encoding="utf-8"))
    assert page_map["zh/classes/EntityPlayer"] == "en/classes/EntityPlayer"
    assert "LLM 智能推断说明：上游文档未提供此描述。" in (output / "zh" / "classes" / "EntityPlayer.md").read_text(encoding="utf-8")
