"""Deterministic work packets for two Luna candidates and one reviewer."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from isaac_wiki.catalog_store import ApiEntry


@dataclass(frozen=True)
class TranslationJob:
    id: str
    entry_id: str
    variant_id: str
    language: str
    mode: str
    source_text: str
    signature: str


def build_translation_jobs(entries: Iterable[ApiEntry]) -> list[TranslationJob]:
    jobs: list[TranslationJob] = []
    for entry in sorted(entries, key=lambda item: item.id):
        for variant in sorted(entry.variants, key=lambda item: item.id):
            english = variant.descriptions.get("en")
            chinese = variant.descriptions.get("zh")
            if english is not None and english.origin == "upstream" and chinese is None:
                specifications = [("zh", mode, english.text) for mode in ("translate-a", "translate-b", "review")]
            elif english is None:
                specifications = [
                    (language, mode, "")
                    for language in ("en", "zh")
                    for mode in ("infer-a", "infer-b", "review")
                ]
            else:
                specifications = []
            jobs.extend(
                TranslationJob(
                    id=f"{entry.id}:{variant.id}:{language}:{mode}",
                    entry_id=entry.id,
                    variant_id=variant.id,
                    language=language,
                    mode=mode,
                    source_text=source_text,
                    signature=variant.signature,
                )
                for language, mode, source_text in specifications
            )
    return jobs
