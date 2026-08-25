from pathlib import Path


def test_weekly_release_is_verified_and_targets_static_site_repository():
    workflow = Path(".github/workflows/weekly-doc-release.yml").read_text(encoding="utf-8")

    assert 'cron: "0 0 * * 1"' in workflow
    assert "pytest tests -q" in workflow
    assert "isaac-wiki build-release-manifest" in workflow
    assert "isaac-wiki export-site" in workflow
    assert "3113y/isaac-llm-wiki" in workflow
    assert "ISAAC_LLM_WIKI_DEPLOY_TOKEN" in workflow
    assert "site-repository/docs/en/" in workflow
    assert "site-repository/docs/zh/" in workflow
    assert "OPENAI_API_KEY" not in workflow
