"""CLI contract tests for profile-aware queries."""

from isaac_wiki.cli import _build_parser


def test_search_command_accepts_profile_options() -> None:
    args = _build_parser().parse_args(
        ["search", "knockback", "--game", "rep+", "--dependency", "rgon", "--language", "zh"]
    )

    assert args.game == "rep+"
    assert args.dependencies == ["rgon"]
    assert args.language == "zh"


def test_sync_reference_command_accepts_a_checkout_path() -> None:
    args = _build_parser().parse_args(["sync-reference", "C:/tmp/isaac-api-edition"])

    assert str(args.source_root).replace("\\", "/").endswith("isaac-api-edition")
