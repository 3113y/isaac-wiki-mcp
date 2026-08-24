"""Definitions and immutable revision locks for imported API sources."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


SOURCE_IDS = {"vanilla-rep", "vanilla-rep-plus", "rgon", "rgon-plus", "eid"}
DEPENDENCIES = {"rgon", "rgon+", "eid"}


@dataclass(frozen=True)
class SourceDefinition:
    id: str
    repository_url: str
    docs_path: str
    game: str
    dependencies: tuple[str, ...]

    def checkout_url(self, revision: str) -> str:
        return f"{self.repository_url}/tree/{revision}"


def _definition(source_id: str, raw: dict[str, Any]) -> SourceDefinition:
    if source_id not in SOURCE_IDS:
        raise ValueError(f"unknown source id: {source_id}")
    game = raw.get("game")
    dependencies = tuple(raw.get("dependencies", []))
    if game not in {"rep", "rep+"}:
        raise ValueError(f"{source_id}: game must be rep or rep+")
    if not set(dependencies).issubset(DEPENDENCIES):
        raise ValueError(f"{source_id}: unsupported dependency")
    if source_id == "rgon" and (game, dependencies) != ("rep", ("rgon",)):
        raise ValueError("rgon must target rep with the rgon dependency")
    if source_id == "rgon-plus" and (game, dependencies) != ("rep+", ("rgon+",)):
        raise ValueError("rgon-plus must target rep+ with the rgon+ dependency")
    if source_id == "eid" and dependencies != ("eid",):
        raise ValueError("eid must declare the eid dependency")
    repository_url = raw.get("repository_url")
    docs_path = raw.get("docs_path")
    if not isinstance(repository_url, str) or not repository_url.startswith("https://github.com/"):
        raise ValueError(f"{source_id}: repository_url must be a GitHub URL")
    if not isinstance(docs_path, str):
        raise ValueError(f"{source_id}: docs_path is required")
    return SourceDefinition(source_id, repository_url, docs_path, game, dependencies)


def load_registry(path: Path) -> dict[str, SourceDefinition]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("source registry must be an object")
    registry = {source_id: _definition(source_id, value) for source_id, value in raw.items() if isinstance(value, dict)}
    if set(registry) != SOURCE_IDS:
        missing = ", ".join(sorted(SOURCE_IDS.difference(registry)))
        raise ValueError(f"source registry missing required source IDs: {missing}")
    return registry


def validate_lock(
    lock: dict[str, dict[str, str]], registry: dict[str, SourceDefinition]
) -> list[str]:
    return [
        source_id
        for source_id in sorted(registry)
        if not re.fullmatch(r"[0-9a-f]{40}", lock.get(source_id, {}).get("revision", ""))
    ]
