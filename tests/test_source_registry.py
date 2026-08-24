import json
from pathlib import Path

import pytest

from isaac_wiki.source_registry import (
    SourceDefinition,
    load_registry,
    validate_lock,
)


def test_rgon_source_uses_the_preserved_repository():
    source = load_registry(Path("data/sources/registry.json"))["rgon"]

    assert source.repository_url == "https://github.com/3113y/REPGON_Docs-Trans-zh_cn"
    assert source.game == "rep"
    assert source.dependencies == ("rgon",)
    assert source.checkout_url("a" * 40).endswith("/tree/" + "a" * 40)


def test_lock_validation_rejects_missing_or_invalid_revisions(tmp_path):
    registry = {
        "eid": SourceDefinition(
            "eid", "https://example.invalid/eid", "api", "rep", ("eid",)
        )
    }
    lock = {"eid": {"revision": "not-a-sha"}}

    assert validate_lock(lock, registry) == ["eid"]


def test_registry_rejects_unknown_dependency_and_invalid_game(tmp_path):
    path = tmp_path / "registry.json"
    path.write_text(
        json.dumps({"bad": {"repository_url": "https://example.invalid", "docs_path": "docs", "game": "afterbirth", "dependencies": ["curllib"]}}),
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        load_registry(path)
