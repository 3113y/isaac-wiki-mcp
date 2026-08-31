"""Build and package a generated Isaac API Edition Markdown snapshot."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def _revision(source_root: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(source_root), "rev-parse", "HEAD"], text=True
    ).strip()


def sync_snapshot(source_root: Path, output: Path) -> dict[str, object]:
    """Build the edition overlay and copy only its bilingual Markdown pages."""

    source_docs = source_root / "docs"
    required = [
        source_docs / "en",
        source_docs / "zh",
        source_docs / "rgon" / "zh",
        source_docs / "rgon-plus" / "en",
        source_root / "scripts" / "build_overlay_docs.py",
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Isaac API Edition checkout is incomplete: {', '.join(missing)}")

    with tempfile.TemporaryDirectory(prefix="isaac-api-edition-overlay-") as temporary:
        generated = Path(temporary) / "docs"
        subprocess.run(
            [
                sys.executable,
                str(source_root / "scripts" / "build_overlay_docs.py"),
                "--source-docs", str(source_docs),
                "--base-en", str(source_docs / "en"),
                "--base-zh", str(source_docs / "zh"),
                "--rgon-zh", str(source_docs / "rgon" / "zh"),
                "--rgon-plus-en", str(source_docs / "rgon-plus" / "en"),
                "--output", str(generated),
            ],
            check=True,
        )
        if output.exists():
            shutil.rmtree(output)
        for language in ("en", "zh"):
            source_language = generated / language
            destination_language = output / language
            for source_page in source_language.rglob("*.md"):
                destination = destination_language / source_page.relative_to(source_language)
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source_page, destination)

    upstream_manifest_path = source_docs / "assets" / "source-release.json"
    upstream_manifest = (
        json.loads(upstream_manifest_path.read_text(encoding="utf-8"))
        if upstream_manifest_path.exists()
        else {}
    )
    counts = {
        language: sum(1 for _ in (output / language).rglob("*.md"))
        for language in ("en", "zh")
    }
    metadata: dict[str, object] = {
        "repository": "https://github.com/3113y/isaac-api-edition",
        "snapshot_revision": _revision(source_root),
        "documents": counts,
        "upstream_sources": upstream_manifest,
    }
    (output / "source-release.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return metadata


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("wiki/reference"))
    args = parser.parse_args()
    print(json.dumps(sync_snapshot(args.source_root.resolve(), args.output.resolve()), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
