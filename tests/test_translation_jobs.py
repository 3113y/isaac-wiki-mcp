from isaac_wiki.catalog_store import ApiEntry
from isaac_wiki.translation_jobs import build_translation_jobs


def _entry(descriptions):
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
                    "descriptions": descriptions,
                }
            ],
        }
    )


def test_existing_upstream_description_creates_only_chinese_translation_jobs():
    entry = _entry({"en": {"text": "Adds heart containers.", "origin": "upstream"}})

    jobs = build_translation_jobs([entry])

    assert {(job.language, job.mode) for job in jobs} == {
        ("zh", "translate-a"),
        ("zh", "translate-b"),
        ("zh", "review"),
    }


def test_missing_description_creates_two_language_inference_jobs_deterministically():
    entry = _entry({})

    jobs = build_translation_jobs([entry])

    assert {(job.language, job.mode) for job in jobs} == {
        (language, mode)
        for language in ("en", "zh")
        for mode in ("infer-a", "infer-b", "review")
    }
    assert jobs == build_translation_jobs([entry])
