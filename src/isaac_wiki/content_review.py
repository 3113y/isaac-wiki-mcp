"""Validation and provenance handling for generated and community text."""

from __future__ import annotations

import re
from dataclasses import dataclass, replace
from typing import Any

from isaac_wiki.catalog_store import ApiEntry, CatalogVariant, Description
from isaac_wiki.translation_jobs import TranslationJob


@dataclass(frozen=True)
class Correction:
    variant_id: str
    language: str
    text: str
    url: str


def validate_content_artifact(
    job: TranslationJob, artifact: dict[str, Any], glossary: dict[str, str]
) -> list[str]:
    errors: list[str] = []
    if artifact.get("job_id") != job.id:
        errors.append("job_id does not match")
    text = artifact.get("text")
    if not isinstance(text, str) or not text.strip():
        errors.append("text is required")
        return errors
    signatures = re.findall(r"\b[\w.]+:[\w.]+\([^\n)]*\)", text)
    if signatures and job.signature not in signatures:
        errors.append("must not contain a modified signature")
    if job.mode.startswith("infer"):
        if artifact.get("origin") != "inferred":
            errors.append("inference artifact must use inferred origin")
        if not artifact.get("inference_basis"):
            errors.append("inferred artifact requires inference_basis")
    elif artifact.get("origin") != "translated":
        errors.append("translation artifact must use translated origin")
    for english, chinese in glossary.items():
        if english in job.source_text and chinese not in text:
            errors.append(f"required terminology missing: {chinese}")
    return errors


def apply_correction(entry: ApiEntry, correction: Correction) -> ApiEntry:
    if correction.language not in {"en", "zh"}:
        raise ValueError("correction language must be en or zh")
    if not correction.text.strip() or not correction.url.startswith("https://github.com/3113y/isaac-wiki-mcp/"):
        raise ValueError("correction requires text and an isaac-wiki-mcp URL")
    variants: list[CatalogVariant] = []
    found = False
    for variant in entry.variants:
        if variant.id != correction.variant_id:
            variants.append(variant)
            continue
        descriptions = dict(variant.descriptions)
        descriptions[correction.language] = Description(
            text=correction.text,
            origin="community_corrected",
            inference_basis=correction.url,
        )
        variants.append(replace(variant, descriptions=descriptions))
        found = True
    if not found:
        raise ValueError(f"unknown variant: {correction.variant_id}")
    return replace(entry, variants=tuple(variants))
