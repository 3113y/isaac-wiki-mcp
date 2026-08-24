# isaac-wiki-mcp

以撒的结合：忏悔(+) 模组 API 文档的 **MCP 知识库服务器**。

采用 llmwiki 架构 —— 文件系统原生的 markdown 页面 + `[[wikilinks]]` 交叉引用。纯 Python 实现，零 ML 依赖，只依赖 `loguru` 一个包。

## 双语、版本感知目录

原有 Markdown Wiki 仍是默认查询来源。指定 `game=rep` 或 `game=rep+` 后，查询会切换到结构化目录；可选依赖为 `rgon`、`rgon+`、`eid`，结果语言可选 `auto`、`zh`、`en`。RGON/RGON+ 覆盖会替代相同的原版 API，EID 则始终作为独立扩展。`include_incompatible=true` 仅用于比较不可用条目，返回结果会标记 `compatible: false`。

LLM 推断描述会在正文末尾附上明确说明。每个目录结果都包含上游仓库、修订版本和源文件。需要纠正翻译或推断时，请提交 issue 或 PR，并附上条目 ID、语言、建议文本、来源及理由；上游原文与修订信息保持不可修改。

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
| `wiki_search` | 全文搜索，返回完整页面内容（不是片段） |
| `wiki_read` | 按名称读取完整类文档，如 `EntityPlayer` |
| `wiki_list` | 按分类列出页面（classes / enums / tutorials） |
| `wiki_stats` | 查看知识库统计数据 |

## 命令行

```bash
isaac-wiki search "player health" --category classes
isaac-wiki read EntityPlayer
isaac-wiki list --category classes
isaac-wiki stats
isaac-wiki build          # 从数据源重建 wiki
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

wiki/               — 生成的 markdown 页面（~1.3MB）
  classes/          — 71 个类页面，含 [[wikilinks]]
  enums/            — 81 个枚举参考页
  tutorials/        — 20 个教程
  index.md          — 全局导航
  llms.txt          — AI 可消费的摘要（llmstxt.org 规范）

data/               — 源数据（wiki_builder 的输入）
```

## 开发

```bash
pip install -e ".[dev]"
pytest tests/ -v
```
