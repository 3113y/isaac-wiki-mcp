"""Structured API variants and profile resolution for the MCP catalog.

The human documentation site exposes two base versions (REP and REP+) and a
single RGON overlay.  This module keeps the same model in a small, immutable
representation so every MCP request can resolve its own explicit profile.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable, Mapping, Sequence


_GAMES = frozenset({"rep", "rep+"})
_DEPENDENCIES = frozenset({"rgon"})
_RELATIONS = frozenset({"base", "extension", "override"})
_DESCRIPTION_ORIGINS = frozenset({"upstream", "translated", "inferred", "community_corrected"})


@dataclass(frozen=True)
class EnvironmentProfile:
    """A caller-selected Isaac API environment."""

    game: str
    dependencies: frozenset[str]

    @classmethod
    def from_values(
        cls, game: str, dependencies: Iterable[str] | None = None
    ) -> "EnvironmentProfile":
        if game not in _GAMES:
            raise ValueError("game must be rep or rep+")
        deps = frozenset(dependencies or ())
        unknown = deps - _DEPENDENCIES
        if unknown:
            raise ValueError(f"unsupported dependencies: {', '.join(sorted(unknown))}")
        return cls(game=game, dependencies=deps)


@dataclass(frozen=True)
class ApiVariant:
    """One versioned implementation of an API member."""

    id: str
    relation: str
    games: frozenset[str]
    dependencies: frozenset[str]
    signature: str
    overrides: str | None = None
    source: "SourceReference | None" = None
    descriptions: Mapping[str, "Description"] | None = None

    def is_compatible(self, profile: EnvironmentProfile) -> bool:
        return profile.game in self.games and self.dependencies <= profile.dependencies

    def validate(self) -> list[str]:
        errors: list[str] = []
        if not self.id:
            errors.append("variant id is required")
        if self.relation not in _RELATIONS:
            errors.append(f"{self.id}: unsupported relation {self.relation!r}")
        if not self.games or not self.games <= _GAMES:
            errors.append(f"{self.id}: games must be a non-empty subset of rep, rep+")
        if not self.dependencies <= _DEPENDENCIES:
            errors.append(f"{self.id}: unsupported dependencies")
        if not self.signature:
            errors.append(f"{self.id}: signature is required")
        if self.relation == "override" and not self.overrides:
            errors.append(f"{self.id}: overrides is required for an override")
        return errors

    def description(self, language: str) -> "Description":
        if not self.descriptions:
            raise KeyError(f"{self.id}: no descriptions")
        return self.descriptions[language]


@dataclass(frozen=True)
class SourceReference:
    repository_url: str
    revision: str
    source_path: str

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "SourceReference":
        return cls(
            repository_url=str(data.get("repository_url", "")),
            revision=str(data.get("revision", "")),
            source_path=str(data.get("source_path", "")),
        )

    def validate(self) -> list[str]:
        errors: list[str] = []
        if not self.repository_url:
            errors.append("source repository_url is required")
        if not self.revision:
            errors.append("source revision is required")
        if not self.source_path:
            errors.append("source source_path is required")
        return errors


@dataclass(frozen=True)
class Description:
    text: str
    origin: str
    inference_basis: str | None = None

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "Description":
        return cls(
            text=str(data.get("text", "")),
            origin=str(data.get("origin", "")),
            inference_basis=(str(data["inference_basis"]) if data.get("inference_basis") else None),
        )

    def validate(self) -> list[str]:
        errors: list[str] = []
        if not self.text:
            errors.append("description text is required")
        if self.origin not in _DESCRIPTION_ORIGINS:
            errors.append(f"unsupported description origin {self.origin!r}")
        if self.origin == "inferred" and not self.inference_basis:
            errors.append("inference_basis is required for inferred text")
        return errors


@dataclass(frozen=True)
class ApiEntry:
    id: str
    title: str
    kind: str
    variants: tuple[ApiVariant, ...]

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "ApiEntry":
        variants: list[ApiVariant] = []
        for raw_variant in data.get("variants", []):
            descriptions = {
                language: Description.from_dict(raw_description)
                for language, raw_description in raw_variant.get("description", {}).items()
            }
            variants.append(ApiVariant(
                id=str(raw_variant.get("id", "")),
                relation=str(raw_variant.get("relation", "")),
                games=frozenset(raw_variant.get("games", [])),
                dependencies=frozenset(raw_variant.get("dependencies", [])),
                signature=str(raw_variant.get("signature", "")),
                overrides=(str(raw_variant["overrides"]) if raw_variant.get("overrides") else None),
                source=SourceReference.from_dict(raw_variant.get("source", {})),
                descriptions=descriptions,
            ))
        return cls(
            id=str(data.get("id", "")),
            title=str(data.get("title", "")),
            kind=str(data.get("kind", "")),
            variants=tuple(variants),
        )

    def validate(self) -> list[str]:
        errors: list[str] = []
        if not self.id:
            errors.append("entry id is required")
        if not self.title:
            errors.append(f"{self.id}: entry title is required")
        if not self.kind:
            errors.append(f"{self.id}: entry kind is required")
        if not self.variants:
            errors.append(f"{self.id}: at least one variant is required")
        for variant in self.variants:
            errors.extend(variant.validate())
            if variant.source:
                errors.extend(f"{variant.id}: {error}" for error in variant.source.validate())
            else:
                errors.append(f"{variant.id}: source is required")
            descriptions = variant.descriptions or {}
            if set(descriptions) != {"en", "zh"}:
                errors.append(f"{variant.id}: bilingual descriptions for en and zh are required")
            for description in descriptions.values():
                errors.extend(f"{variant.id}: {error}" for error in description.validate())
        return errors


def resolve_variants(
    variants: Sequence[ApiVariant], profile: EnvironmentProfile
) -> list[ApiVariant]:
    """Return members available to *profile*, applying explicit overrides.

    A RGON override replaces only the exact declared base identifier.  RGON
    extensions without ``overrides`` remain alongside the base API.
    """

    active = [variant for variant in variants if variant.is_compatible(profile)]
    replaced = {
        variant.overrides
        for variant in active
        if variant.relation == "override" and variant.overrides
    }
    return [variant for variant in active if variant.id not in replaced]
