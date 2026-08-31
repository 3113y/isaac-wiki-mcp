"""MCP tool contract tests."""

from isaac_wiki.server import TOOLS


def test_search_advertises_profile_arguments() -> None:
    tool = next(item for item in TOOLS if item["name"] == "wiki_search")
    properties = tool["inputSchema"]["properties"]

    assert properties["game"]["enum"] == ["rep", "rep+"]
    assert properties["dependencies"]["items"]["enum"] == ["rgon"]
    assert properties["language"]["enum"] == ["en", "zh", "auto"]


def test_sources_tool_is_available() -> None:
    assert any(item["name"] == "wiki_sources" for item in TOOLS)
