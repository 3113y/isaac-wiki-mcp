# One-time Luna document polish

## Goal

Produce a reviewed, human-maintained static API documentation snapshot. This
one migration may use low-cost Luna subagents to polish API prose at scale.
Subsequent changes are made directly to Markdown by people and published by
GitHub Actions without model calls or automatic upstream overwrites.

## Input and output

- Input: the synced English and Chinese API Markdown snapshots, including the
  original source provenance.
- Output: the same Markdown paths, with only explanatory prose improved.
- Each model-generated or model-inferred explanation must carry an explicit
  attribution note in the language of the page.
- A deterministic validator rejects a changed API signature, code block,
  badge, link target, front matter, heading structure, or file path.

## Luna worker contract

Workers receive small, non-overlapping batches of Markdown files and a strict
prompt. They may improve clarity, terminology, grammar, and sentence
structure. They must not invent API behavior, add undocumented compatibility,
translate code, alter examples, or change Markdown structure. If an English
source explanation is absent, the worker may infer a concise explanation from
the function or method name and must mark it as inferred.

## Publishing lifecycle

1. The one-time migration produces reviewed Markdown and a provenance manifest.
2. The documentation repository commits that snapshot.
3. GitHub Actions runs only strict build and deployment on push or manual
   dispatch. It does not fetch upstream documentation and does not invoke a
   model.
4. Future documentation corrections are ordinary Markdown edits followed by a
   push, so no automated process overwrites human changes.

## RGON and RGON+

The static site stores dedicated document roots for RGON (REP dependency) and
RGON+ (REP+ dependency). The profile control navigates to the selected root;
it never presents vanilla content as extension content. Missing-language pages
remain visible with a clear source/fallback notice until separately curated.

## Verification

- Tests compare protected Markdown tokens before and after polishing.
- Tests confirm every inferred note is explicit.
- Tests verify profile routing reaches real RGON/RGON+ document roots.
- `mkdocs build --strict` must succeed before commit.
