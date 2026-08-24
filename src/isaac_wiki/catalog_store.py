"""Validated, bilingual persistence for version-aware Isaac API records."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from isaac_wiki.catalog import ApiVariant


DESCRIPTION_ORIGINS = {"upstream", "translated", "inferred", "community_corrected"}
RELATIONS = {"base", "extension", "override"}


@dataclass(frozen=True)
class Description:
    text: str
    origin: str
    inference_basis: str | None = None


@dataclass(frozen=True)
class SourceMetadata:
    repository_url: str | None
    revision: str | None
    source_path: str | None


@dataclass(frozen=True)
class CatalogVariant:
    id: str
    relation: str
    game: str
    dependencies: tuple[str, ...]
    signature: str
    source: SourceMetadata
    descriptions: dict[str, Description]
    overrides: str | None = None

    def description(self, language: str) -> Description:
        return self.descriptions[language]

    def to_api_variant(self) -> ApiVariant:
        return ApiVariant(
            id=self.id,
            relation=self.relation,
            game=self.game,
            dependencies=self.dependencies,
            signature=self.signature,
            overrides=self.overrides,
        )


@dataclass(frozen=True)
class ApiEntry:
    id: str
    kind: str
    signature: str
    variants: tuple[CatalogVariant, ...]
    issues: tuple[str, ...] = ()

    @classmethod
    def from_dict(cls, value: Any) -> "ApiEntry":
        if not isinstance(value, dict):
            return cls("", "", "", (), ("entry must be a JSON object",))

        variants: list[CatalogVariant] = []
        issues: list[str] = []
        raw_variants = value.get("variants", [])
        if not isinstance(raw_variants, list):
            return cls(
                value.get("id", ""),
                value.get("kind", ""),
                value.get("signature", ""),
                (),
                ("variants must be an array",),
            )
        for index, raw in enumerate(raw_variants):
            if not isinstance(raw, dict):
                issues.append(f"variants[{index}] must be an object")
                continue
            environment = raw.get("environment", {})
            source = raw.get("source", {})
            if not isinstance(environment, dict):
                issues.append(f"variants[{index}].environment must be an object")
                environment = {}
            if not isinstance(source, dict):
                issues.append(f"variants[{index}].source must be an object")
                source = {}
            raw_descriptions = raw.get("descriptions", {})
            if not isinstance(raw_descriptions, dict):
                issues.append(f"variants[{index}].descriptions must be an object")
                raw_descriptions = {}
            raw_dependencies = environment.get("dependencies", [])
            if not isinstance(raw_dependencies, list):
                issues.append(f"variants[{index}].environment.dependencies must be an array")
                raw_dependencies = []
            descriptions = {
                language: Description(
                    text=description.get("text", ""),
                    origin=description.get("origin", ""),
                    inference_basis=description.get("inference_basis"),
                )
                for language, description in raw_descriptions.items()
                if isinstance(description, dict)
            }
            variants.append(
                CatalogVariant(
                    id=raw.get("id", ""),
                    relation=raw.get("relation", ""),
                    game=environment.get("game", ""),
                    dependencies=tuple(raw_dependencies),
                    signature=raw.get("signature", value.get("signature", "")),
                    source=SourceMetadata(
                        repository_url=source.get("repository_url"),
                        revision=source.get("revision"),
                        source_path=source.get("source_path"),
                    ),
                    descriptions=descriptions,
                    overrides=raw.get("overrides"),
                )
            )
        return cls(
            id=value.get("id", ""),
            kind=value.get("kind", ""),
            signature=value.get("signature", ""),
            variants=tuple(variants),
            issues=tuple(issues),
        )


class CatalogStore:
    """Loads catalog JSON files and reports deterministic validation errors."""

    def __init__(self, catalog_dir: str | Path):
        self.catalog_dir = Path(catalog_dir)

    def _paths(self) -> list[Path]:
        return sorted(
            path
            for path in self.catalog_dir.glob("*.json")
            if path.name != "schema.json"
        )

    def entries(self) -> list[ApiEntry]:
        return [
            ApiEntry.from_dict(json.loads(path.read_text(encoding="utf-8")))
            for path in self._paths()
        ]

    def validate(self) -> list[str]:
        errors: list[str] = []
        try:
            entries = self.entries()
        except (OSError, json.JSONDecodeError, TypeError) as exc:
            return [f"catalog read error: {exc}"]

        all_variant_ids = {
            variant.id for entry in entries for variant in entry.variants if variant.id
        }
        for entry in entries:
            errors.extend(entry.issues)
            if not entry.id:
                errors.append("entry id is required")
            if not entry.variants:
                errors.append(f"{entry.id or '<unknown>'}: at least one variant is required")
            for variant in entry.variants:
                prefix = f"{entry.id or '<unknown>'}/{variant.id or '<unknown>'}"
                if variant.relation not in RELATIONS:
                    errors.append(f"{prefix}: relation must be one of {sorted(RELATIONS)}")
                if variant.game not in {"rep", "rep+"}:
                    errors.append(f"{prefix}: game must be rep or rep+")
                unsupported = [
                    dependency
                    for dependency in variant.dependencies
                    if not isinstance(dependency, str)
                    or dependency not in {"eid", "rgon", "rgon+"}
                ]
                if unsupported:
                    values = ", ".join(sorted(repr(item) for item in unsupported))
                    errors.append(f"{prefix}: unsupported dependencies: {values}")
                if variant.source.repository_url is None:
                    errors.append(f"{prefix}: source.repository_url is required")
                if not variant.source.revision:
                    errors.append(f"{prefix}: source.revision is required")
                elif not re.fullmatch(r"[0-9a-f]{40}", variant.source.revision):
                    errors.append(f"{prefix}: source.revision must be a 40-character Git SHA")
                if variant.source.source_path is None:
                    errors.append(f"{prefix}: source.source_path is required")
                for language in ("en", "zh"):
                    description = variant.descriptions.get(language)
                    if description is None:
                        errors.append(f"{prefix}: descriptions.{language} is required")
                        continue
                    if not description.text:
                        errors.append(f"{prefix}: descriptions.{language}.text is required")
                    if description.origin not in DESCRIPTION_ORIGINS:
                        errors.append(f"{prefix}: descriptions.{language}.origin is invalid")
                    if description.origin == "inferred" and not description.inference_basis:
                        errors.append(
                            f"{prefix}: descriptions.{language}.inference_basis is required for inferred text"
                        )
                if variant.relation == "override":
                    if not variant.overrides or variant.overrides not in all_variant_ids:
                        errors.append(f"{prefix}: overrides references an unknown variant: {variant.overrides}")
        return errors
