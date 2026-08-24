from isaac_wiki.catalog_store import ApiEntry
from isaac_wiki.content_review import Correction, apply_correction, validate_content_artifact
from isaac_wiki.translation_jobs import TranslationJob


def _entry():
    return ApiEntry.from_dict(
        {
            "id": "player.add_hearts",
            "kind": "method",
            "signature": "EntityPlayer:AddHearts(amount)",
            "variants": [
                {
                    "id": "player.add_hearts",
                    "relation": "base",
                    "environment": {"game": "rep", "dependencies": []},
                    "signature": "EntityPlayer:AddHearts(amount)",
                    "source": {},
                    "descriptions": {
                        "en": {"text": "Adds heart containers.", "origin": "upstream"},
                        "zh": {"text": "添加心之容器。", "origin": "translated"},
                    },
                }
            ],
        }
    )


def test_rejects_rewritten_signature():
    job = TranslationJob("job", "player.add_hearts", "player.add_hearts", "zh", "translate-a", "", "EntityPlayer:AddHearts(amount)")
    artifact = {"job_id": job.id, "text": "EntityPlayer:AddHearts(count)", "origin": "translated"}

    assert "must not contain a modified signature" in validate_content_artifact(job, artifact, {})


def test_community_correction_sets_provenance():
    correction = Correction("player.add_hearts", "zh", "添加红心容器。", "https://github.com/3113y/isaac-wiki-mcp/issues/1")

    updated = apply_correction(_entry(), correction)

    assert updated.variants[0].description("zh").origin == "community_corrected"
