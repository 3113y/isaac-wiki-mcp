import pytest

from isaac_wiki.catalog import ApiVariant, EnvironmentProfile, resolve_variants


def test_rgon_override_replaces_rep_base_member():
    profile = EnvironmentProfile.from_values("rep", ["rgon"])
    base = ApiVariant("player.add_hearts", "base", "rep", (), "EntityPlayer:AddHearts(amount)")
    override = ApiVariant(
        "rgon.player.add_hearts",
        "override",
        "rep",
        ("rgon",),
        "EntityPlayer:AddHearts(amount)",
        overrides="player.add_hearts",
    )
    assert resolve_variants([base, override], profile) == [override]


@pytest.mark.parametrize(
    ("game", "dependencies"),
    [("rep+", ["rgon"]), ("rep", ["rgon+"])],
)
def test_rejects_invalid_rgon_game_combinations(game, dependencies):
    with pytest.raises(ValueError):
        EnvironmentProfile.from_values(game, dependencies)


def test_rejects_unknown_dependencies():
    with pytest.raises(ValueError, match="unsupported dependencies"):
        EnvironmentProfile.from_values("rep", ["typo"])


def test_eid_extension_is_active_when_dependency_is_enabled():
    profile = EnvironmentProfile.from_values("rep", ["eid"])
    variant = ApiVariant("eid.player.foo", "extension", "rep", ("eid",), "Player:Foo()")
    assert resolve_variants([variant], profile) == [variant]


def test_non_overriding_extension_remains_alongside_base():
    profile = EnvironmentProfile.from_values("rep", ["eid"])
    base = ApiVariant("player.foo", "base", "rep", (), "Player:Foo()")
    extension = ApiVariant("eid.player.foo_extra", "extension", "rep", ("eid",), "Player:FooExtra()")
    assert resolve_variants([base, extension], profile) == [base, extension]
