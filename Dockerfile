# ──────────────────────────────────────────────────────────────
# Isaac RAG MCP Server — Docker image (wiki-first, slim)
# ──────────────────────────────────────────────────────────────
FROM python:3.12-slim

LABEL org.opencontainers.image.title="isaac-wiki-mcp"
LABEL org.opencontainers.image.description="MCP server providing wiki-style full-text search over Binding of Isaac modding API docs"

# ── Use Tsinghua mirror for Debian ─────────────────────────────
RUN sed -i 's|deb.debian.org|mirrors.tuna.tsinghua.edu.cn|g' /etc/apt/sources.list.d/debian.sources 2>/dev/null; \
    sed -i 's|http://deb.debian.org|http://mirrors.tuna.tsinghua.edu.cn|g' /etc/apt/sources.list 2>/dev/null; \
    true

# No system-level ML libs needed — wiki engine is pure Python

WORKDIR /app

# ── Pip mirror shortcut ────────────────────────────────────────
ENV PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple

# ── Install Python deps (wiki-only: no numpy/faiss/sentence-transformers) ──
RUN pip install loguru pyyaml

# ── Copy app code + wiki data ──────────────────────────────────
COPY src/ src/
COPY data/ data/
COPY wiki/ wiki/

# ── No need to "pip install ." — just add src to path ──────────
ENV PYTHONPATH=/app/src

ENV PYTHONUNBUFFERED=1

# MCP server on stdio
ENTRYPOINT ["python", "-m", "isaac_wiki.server"]
