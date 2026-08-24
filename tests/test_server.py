from isaac_wiki.server import TOOLS


def test_tools_list_advertises_profile_arguments():
    tool = next(item for item in TOOLS if item["name"] == "wiki_search")
    properties = tool["inputSchema"]["properties"]
    assert properties["language"]["enum"] == ["auto", "zh", "en"]
    assert properties["game"]["enum"] == ["rep", "rep+"]
    assert properties["dependencies"]["items"]["enum"] == ["rgon", "rgon+", "eid"]
    assert properties["include_incompatible"]["type"] == "boolean"


def test_read_and_list_tools_advertise_same_profile_arguments():
    for name in ("wiki_read", "wiki_list"):
        tool = next(item for item in TOOLS if item["name"] == name)
        properties = tool["inputSchema"]["properties"]
        assert {"game", "dependencies", "language", "include_incompatible"} <= set(properties)
