"""Environment-aware records for the Binding of Isaac API catalog."""

from dataclasses import dataclass
from typing import Iterable, Sequence


@dataclass(frozen=True)
class EnvironmentProfile:
    game: str
    dependencies: frozenset[str]

    @classmethod
    def from_values(
        cls, game: str, dependencies: Iterable[str] | None = None
    ) -> "EnvironmentProfile":
        deps = frozenset(dependencies or ())
        if game not in {"rep", "rep+"}:
            raise ValueError("game must be rep or rep+")
        unsupported = deps.difference({"eid", "rgon", "rgon+"})
        if unsupported:
            values = ", ".join(sorted(unsupported))
            raise ValueError(f"unsupported dependencies: {values}")
        if "rgon" in deps and game != "rep":
            raise ValueError("rgon requires rep")
        if "rgon+" in deps and game != "rep+":
            raise ValueError("rgon+ requires rep+")
        return cls(game, deps)


@dataclass(frozen=True)
class ApiVariant:
    id: str
    relation: str
    game: str
    dependencies: tuple[str, ...]
    signature: str
    overrides: str | None = None

    def is_compatible(self, profile: EnvironmentProfile) -> bool:
        return self.game == profile.game and set(self.dependencies).issubset(
            profile.dependencies
        )


def resolve_variants(
    variants: Sequence[ApiVariant], profile: EnvironmentProfile
) -> list[ApiVariant]:
    active = [item for item in variants if item.is_compatible(profile)]
    replaced = {
        item.overrides
        for item in active
        if item.relation == "override" and item.overrides
    }
    return [item for item in active if item.id not in replaced]
