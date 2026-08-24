import json

from isaac_wiki.release_manifest import build_release_manifest


def test_manifest_has_source_revisions_and_environments(tmp_path):
    catalog = tmp_path / "catalog"
    catalog.mkdir()
    (catalog / "entry.json").write_text(
        json.dumps(
            {
                "id": "player.foo",
                "kind": "method",
                "signature": "EntityPlayer:Foo()",
                "variants": [
                    {
                        "id": "player.foo",
                        "relation": "base",
                        "environment": {"game": "rep", "dependencies": []},
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    lock = tmp_path / "lock.json"
    lock.write_text(json.dumps({"eid": {"revision": "a" * 40}}), encoding="utf-8")

    manifest = build_release_manifest(catalog, lock)

    assert set(manifest) >= {"catalog_revision", "sources", "published_at", "affected_environments"}
    assert manifest["sources"]["eid"] == "a" * 40
    assert manifest["affected_environments"] == [{"game": "rep", "dependencies": []}]
