"""Build the immutable metadata consumed by the weekly documentation release."""

from __future__ import annotations

import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


def build_release_manifest(catalog_dir: Path, source_lock: Path) -> dict[str, Any]:
    digest = hashlib.sha256()
    environments: set[tuple[str, tuple[str, ...]]] = set()
    for path in sorted(catalog_dir.glob("*.json")):
        if path.name == "schema.json":
            continue
        content = path.read_bytes()
        digest.update(path.name.encode("utf-8"))
        digest.update(content)
        entry = json.loads(content)
        for variant in entry.get("variants", []):
            environment = variant.get("environment", {})
            environments.add(
                (environment.get("game", ""), tuple(environment.get("dependencies", [])))
            )
    lock = json.loads(source_lock.read_text(encoding="utf-8"))
    return {
        "catalog_revision": digest.hexdigest(),
        "sources": {key: value["revision"] for key, value in sorted(lock.items())},
        "published_at": datetime.now(UTC).isoformat(),
        "affected_environments": [
            {"game": game, "dependencies": list(dependencies)}
            for game, dependencies in sorted(environments)
        ],
    }
