# Task 1 Report: Catalog records and environment resolution

## Scope

Implemented `EnvironmentProfile`, `ApiVariant`, and `resolve_variants` in `src/isaac_wiki/catalog.py`. Added focused coverage in `tests/test_catalog.py` for override replacement, invalid RGON/game combinations, EID extensions, and non-overriding extensions.

## TDD evidence

The initial focused run failed during collection as expected because the production module did not exist:

```text
ModuleNotFoundError: No module named 'isaac_wiki.catalog'
```

After the minimal implementation, the focused suite passed:

```text
5 passed in 0.03s
```

The worktree's copied `.venv` points at a host interpreter and `uv run --extra dev pytest tests/test_catalog.py -q` could not launch its pytest executable. Verification therefore used the same Python 3.12 interpreter directly with `PYTHONPATH=src`.

## Full verification

```text
31 passed in 0.31s
```

## Design notes

- A variant is active only when its game matches and all declared dependencies are enabled.
- Active override variants remove the variant identified by `overrides`, while unrelated extensions remain in catalog order.
- `rgon` is valid only for `rep`; `rgon+` is valid only for `rep+`.
