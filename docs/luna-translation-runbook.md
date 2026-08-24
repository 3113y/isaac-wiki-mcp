# Luna translation runbook

For every translation or inference job, run two independent Luna workers for the `*-a` and `*-b` jobs. A third Luna worker receives the same bounded source context plus both candidate JSON responses and resolves the `review` job. Workers must return only JSON for their job ID; they must not edit catalog facts or repository files.

Validate the reviewer output with `validate_content_artifact` before merging it into a catalog entry. Preserve signatures, parameter names, code blocks, source metadata, environment fields, and all protected tokens. Existing upstream English text receives only a Chinese translation. Missing upstream descriptions receive independently inferred English and Chinese text, both marked `inferred` so the published suffix is appended automatically.
