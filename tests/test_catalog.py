"""Tests for version-aware API catalog resolution."""

import pytest

from isaac_wiki.catalog import ApiVariant, EnvironmentProfile, resolve_variants


def test_rgon_override_replaces_its_base_member() -> None:
    profile = EnvironmentProfile.from_values("rep", ["rgon"])
    base = ApiVariant(
        id="entity.add_knockback",
        relation="base",
        games=frozenset({"rep", "rep+"}),
        dependencies=frozenset(),
        signature="Entity:AddKnockback(entity, force)",
    )
    override = ApiVariant(
        id="rgon.entity.add_knockback",
        relation="override",
        games=frozenset({"rep"}),
        dependencies=frozenset({"rgon"}),
        signature="Entity:AddKnockback(entity, force, direction)",
        overrides="entity.add_knockback",
    )

    assert resolve_variants([base, override], profile) == [override]


def test_rgon_extensions_can_be_selected_with_rep_or_rep_plus() -> None:
    assert EnvironmentProfile.from_values("rep", ["rgon"]).dependencies == frozenset({"rgon"})
    assert EnvironmentProfile.from_values("rep+", ["rgon"]).dependencies == frozenset({"rgon"})


def test_invalid_game_and_unknown_dependency_are_rejected() -> None:
    with pytest.raises(ValueError, match="game must be rep or rep\\+"):
        EnvironmentProfile.from_values("ab+")
    with pytest.raises(ValueError, match="unsupported dependencies"):
        EnvironmentProfile.from_values("rep", ["eid"])


def test_non_overriding_rgon_member_is_added_to_the_base_result() -> None:
    profile = EnvironmentProfile.from_values("rep", ["rgon"])
    base = ApiVariant("entity.add_velocity", "base", frozenset({"rep"}), frozenset(), "Entity:AddVelocity(velocity)")
    extension = ApiVariant("rgon.entity.new_helper", "extension", frozenset({"rep"}), frozenset({"rgon"}), "Entity:NewHelper()")

    assert resolve_variants([base, extension], profile) == [base, extension]
