# isaac-wiki-mcp

以撒的结合：忏悔(+) 模组 API 文档的 **MCP 知识库服务器**。内置锁定版本的 [Isaac API Edition](https://github.com/3113y/isaac-api-edition) 双语 Markdown 快照，可在每次请求中明确选择 REP、REP+ 与 RGON。

采用 llmwiki 架构 —— 文件系统原生的 markdown 页面 + `[[wikilinks]]` 交叉引用。纯 Python 实现，零 ML 依赖，只依赖 `loguru` 一个包。

## 解决了什么问题

用 AI 写以撒模组时，LLM 会编造不存在的 API 方法名和参数。这个项目把 72 个类、1,554 个方法的完整 API 文档做成了可搜索的知识库，让 AI 能查到**完整的类页面**（不是碎片化的 chunk），避免幻觉。

## 快速上手

```bash
pip install isaac-wiki-mcp
```

然后在 Claude Code 的 MCP 配置里加上（`~/.claude/mcp.json`）：

```json
{
  "mcpServers": {
    "isaac-wiki": {
      "command": "uvx",
      "args": ["isaac-wiki-mcp"]
    }
  }
}
```

也可以用 Docker：

```json
{
  "mcpServers": {
    "isaac-wiki": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "ghcr.io/你的用户名/isaac-wiki-mcp"]
    }
  }
}
```

## MCP 工具

| 工具 | 功能 |
|------|------|
| `wiki_search` | 全文搜索，按语言与 API 配置返回完整页面内容（不是片段） |
| `wiki_read` | 按名称读取完整页面，如 `EntityPlayer` 或 `enums/EntityType` |
| `wiki_list` | 按分类、语言与 API 配置列出页面 |
| `wiki_stats` | 查看知识库统计数据 |
| `wiki_sources` | 查看打包快照的来源仓库、锁定 revision 与支持的配置 |

`wiki_search`、`wiki_read` 与 `wiki_list` 接受这些可选参数：

```json
{
  "game": "rep",
  "dependencies": ["rgon"],
  "language": "en"
}
```

- `game`：`rep` 或 `rep+`；未指定时为 `rep`。
- `dependencies`：目前仅支持 `rgon`。未启用时返回内容会移除 RGON 覆写/新增块。
- `language`：`en`、`zh` 或 `auto`。`auto` 仅按查询文本保守判断；需要英文原文时请明确传 `en`。

## 命令行

```bash
isaac-wiki search "player health" --category classes
isaac-wiki read EntityPlayer
isaac-wiki list --category classes
isaac-wiki stats
isaac-wiki build          # 从数据源重建 wiki
isaac-wiki search "knockback" --game rep --language en
isaac-wiki read Entity --game rep+ --dependency rgon --language zh
isaac-wiki sync-reference /path/to/isaac-api-edition
```

## 数据规模

| 分类 | 数量 |
|------|------|
| 类 | 71 |
| 方法 | 1,554 |
| 枚举 | 81 |
| 教程 | 20 |
| 总页面 | 173 |

每个类页面包含：概述、继承链、关联类型（带 `[[wikilinks]]`）、所有方法的签名、DLC 兼容标记、使用场景。

## 架构

```
src/isaac_wiki/
  wiki_builder.py   — 数据清洗 + JSON → wiki markdown 转换
  wiki_engine.py    — 全文搜索 + 页面读取（纯 Python）
  facade.py         — 对外 API 层（永不抛异常）
  server.py         — MCP stdio 服务器（4 个工具）
  cli.py            — 命令行工具

wiki/               — 生成的 markdown 页面与 API Edition 快照
  classes/          — 71 个类页面，含 [[wikilinks]]
  enums/            — 81 个枚举参考页
  tutorials/        — 20 个教程
  index.md          — 全局导航
  llms.txt          — AI 可消费的摘要（llmstxt.org 规范）
  reference/
    en/             — 英文原文优先的 API Edition 快照
    zh/             — 中文 API Edition 快照
    source-release.json — 锁定来源 revision 与上游清单

data/               — 旧 Wiki 构建输入与版本化 catalog 种子
```

## 开发

```bash
pip install -e ".[dev]"
pytest tests/ -v
```
