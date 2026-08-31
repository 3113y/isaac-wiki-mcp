# Isaac Wiki MCP

面向《以撒的结合：忏悔》模组开发的 MCP 文档服务器。它将 API 文档作为本地 Markdown 知识库提供给支持 MCP 的编码助手，便于在 Vibe Coding 时查证类、方法、枚举与教程，减少凭空编造 API 的情况。

项目采用 [llmwiki](https://github.com/3113y/isaac-wiki-mcp) 风格：文档是可审阅、可版本控制的 Markdown 页面，并保留 `[[wikilinks]]` 交叉引用；检索为纯 Python 全文搜索，不依赖向量数据库或模型服务。

## 当前内容与适用范围

- 内置锁定版本的 [Isaac API Edition](https://github.com/3113y/isaac-api-edition) 中英文 Markdown 快照。
- 通过请求配置选择基础游戏 API：`rep` 或 `rep+`。
- 可启用 `rgon` 注入型 API 覆盖层；未启用时，RGON 标记区块会从返回内容中移除。
- `language` 支持 `en`、`zh` 与 `auto`。`auto` 会根据查询文本保守地判断中英文；需要稳定结果时应显式指定语言。
- 每次配置了 `game`、`dependencies` 或非 `auto` 的 `language`，检索都会使用版本化双语快照；不传这些参数时保持旧版 `wiki/` 查询行为，以兼容既有调用方。

当前 MCP 对外支持的依赖只有 `rgon`。快照构建过程会记录 RGON 与 RGON+ 的上游来源，但 RGON+、EID、curlib 等尚不是可选择的 MCP 依赖配置；请不要将它们视为本版本的兼容性承诺。

当前快照记录：中英文各 468 篇 Markdown 文档，API Edition 快照修订为 `77199a65ab2ebd789ecefb88a66220811855a238`。可调用 `wiki_sources` 读取机器可用的完整来源、页面数和上游修订信息。

## 安装

要求 Python 3.11 或更高版本。使用 [uv](https://docs.astral.sh/uv/) 的本地开发安装：

```bash
git clone https://github.com/3113y/isaac-wiki-mcp.git
cd isaac-wiki-mcp
uv sync --extra dev
```

也可以使用 pip：

```bash
pip install -e ".[dev]"
```

## 配置为 MCP 服务器

服务器通过标准输入输出传输 JSON-RPC，日志只写入标准错误。以本地克隆目录为例，在 MCP 客户端配置中加入：

```json
{
  "mcpServers": {
    "isaac-wiki": {
      "command": "uv",
      "args": ["run", "isaac-wiki-mcp"],
      "cwd": "/absolute/path/to/isaac-wiki-mcp"
    }
  }
}
```

也可在已激活的 Python 环境中将 `command` 改为 `isaac-wiki-mcp`。配置完成后，让编码助手先调用 `wiki_search` 找到页面，再用 `wiki_read` 取得完整上下文。

## MCP 工具

| 工具 | 用途 | 主要参数 |
| --- | --- | --- |
| `wiki_search` | 全文搜索并返回匹配页面的完整内容 | `query`、`top_k`（1–10）、`category`、环境参数 |
| `wiki_read` | 按页面名或路径读取完整页面 | `page`、环境参数 |
| `wiki_list` | 列出页面元数据，不返回正文 | `category`、环境参数 |
| `wiki_stats` | 返回本地索引的基础统计（分类计数基于历史 wiki 目录） | 无 |
| `wiki_sources` | 返回快照仓库、支持的配置和锁定修订 | 无 |

`category` 可取 `classes`、`enums`、`tutorials` 或 `reference`。它用于历史 `wiki/` 目录的分类过滤；版本化快照沿用 API Edition 的原始目录层级，当前不会再按该参数二次过滤。环境参数在 `wiki_search`、`wiki_read` 与 `wiki_list` 中一致：

| 参数 | 取值 | 说明 |
| --- | --- | --- |
| `game` | `rep`、`rep+` | 基础 API 版本；省略时配置记录为 `rep` |
| `dependencies` | `[]` 或 `["rgon"]` | 要启用的 API 覆盖层 |
| `language` | `en`、`zh`、`auto` | 返回文档语言；`auto` 根据查询或页面名判断 |

`wiki_search` 与 `wiki_read` 还接受 `include_incompatible`。该字段目前会随结果回显，用于未来的条目级兼容性筛选；当前版本不应把它当作已完成的跨配置过滤功能。

### 调用示例

查询 REP 的英文页面：

```json
{
  "query": "player health",
  "game": "rep",
  "language": "en"
}
```

读取 REP+ 的中文 `EntityPlayer` 页面：

```json
{
  "page": "EntityPlayer",
  "game": "rep+",
  "language": "zh"
}
```

在 REP 环境中检索 RGON 覆盖层内容：

```json
{
  "query": "knockback",
  "game": "rep",
  "dependencies": ["rgon"],
  "language": "auto"
}
```

建议调用方始终传入实际开发环境的 `game`、`dependencies` 和 `language`，并将工具返回的 `profile` 视作本次查询采用的环境记录。

## 命令行

`isaac-wiki` 可用于本地检查知识库：

```bash
# 搜索并以 JSON 返回
uv run isaac-wiki search "player health" --game rep --language en --format json

# 读取中文版页面
uv run isaac-wiki read EntityPlayer --game rep+ --language zh

# 使用 RGON 覆盖层列出版本化页面
uv run isaac-wiki list --game rep --dependency rgon --language zh --format json

# 查看本地索引统计
uv run isaac-wiki stats --format json
```

常用命令：

```text
isaac-wiki search QUERY [--top-k N] [--category CATEGORY]
isaac-wiki read PAGE
isaac-wiki list [--category CATEGORY]
isaac-wiki stats
isaac-wiki build
isaac-wiki sync-reference SOURCE_ROOT [--output wiki/reference]
```

`search` 和 `read` 支持 `--include-incompatible`；环境选项为 `--game rep|rep+`、可重复的 `--dependency rgon`，以及 `--language en|zh|auto`。

## 数据来源与更新

版本化快照位于 `wiki/reference/en` 和 `wiki/reference/zh`，其来源清单为 `wiki/reference/source-release.json`。更新 API Edition 后，可在完整的本地 `isaac-api-edition` 检出目录中重新生成并打包快照：

```bash
uv run isaac-wiki sync-reference /path/to/isaac-api-edition
```

该命令需要上游目录具备基础中英文文档、RGON/RGON+ 文档以及 `scripts/build_overlay_docs.py`。它会重建 `wiki/reference` 并更新来源修订记录；运行前请确认上游检出内容完整。提交快照更新时应同时检查 `source-release.json`，让使用者能够追溯文档版本。

API 文档的错误或改进建议欢迎通过 Issue 或 Pull Request 提交。请提供页面路径、原文来源、适用的 `game` / `dependencies` 配置，以及可验证的修改依据；这能避免将不同版本或前置依赖的行为混入同一条说明。

## 项目结构

```text
src/isaac_wiki/
  server.py          MCP stdio JSON-RPC 服务器
  facade.py          统一查询接口与环境解析
  wiki_engine.py     Markdown 索引、搜索、读取与 RGON 内容过滤
  snapshot.py        API Edition 快照构建与来源记录
  cli.py             命令行入口
wiki/
  reference/en/      版本化英文 API Edition 快照
  reference/zh/      版本化中文 API Edition 快照
  reference/source-release.json
data/                旧版页面生成所用数据
tests/               自动化测试
```

## 开发与验证

```bash
uv run --extra dev pytest tests -q
```

项目以 MIT License 发布。
