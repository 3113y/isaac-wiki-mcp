# API translation job

Translate only the supplied description into Chinese. Preserve every API identifier, signature, parameter name, code block, Markdown link, and literal value. Follow the supplied terminology table. Return JSON with `job_id`, `text`, and `origin: "translated"`. Do not edit repository files or infer APIs that are absent from the source.
