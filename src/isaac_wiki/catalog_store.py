"""Validated on-disk storage for versioned bilingual API catalog entries."""

from __future__ import annotations

import json
from pathlib import Path

from isaac_wiki.catalog import ApiEntry


class CatalogStore:
    """Read immutable JSON catalog entries from a directory."""

    def __init__(self, catalog_dir: str | Path):
        self.catalog_dir = Path(catalog_dir)

    def entries(self) -> list[ApiEntry]:
        if not self.catalog_dir.exists():
            return []
        paths = sorted(path for path in self.catalog_dir.glob("*.json") if path.name != "schema.json")
        return [ApiEntry.from_dict(json.loads(path.read_text(encoding="utf-8"))) for path in paths]

    def validate(self) -> list[str]:
        errors: list[str] = []
        try:
            entries = self.entries()
        except (json.JSONDecodeError, OSError, TypeError, ValueError) as exc:
            return [str(exc)]
        for entry in entries:
            errors.extend(entry.validate())
        return errors
