# 双语以撒 API LLM Wiki 设计

## 目标

将现有原版 API Wiki 扩展为面向《以撒的结合》Mod 开发的双语 LLM Wiki：降低编码 Agent 对 API 签名、适用版本和依赖关系的幻觉，同时生成面向人类的 GitHub Pages 文档站。

第一期覆盖原版 `REP` / `REP+`、旧版 `RGON`、新版 `RGON+` 与 `EID`。CurLib 暂不纳入。

## 架构

所有上游资料先转换为一套规范化双语文档数据，再由两个消费者使用：

```text
上游 Markdown、Lua 源码与文档站
        ↓
清洗、归属、翻译、推断与校验
        ↓
规范化双语 API 数据
        ├── LLM Wiki MCP
        └── GitHub Pages 双语静态站
```

不按环境复制整套页面。每个 API 有稳定规范 ID，所有版本变体、描述与来源集中在该条目中。这样可避免原版和 RGON 页面漂移。

## 资料源与环境

| 范围 | 资料源 | 关系 |
| --- | --- | --- |
| 原版 REP / REP+ | 现有 Isaac API 文档及其上游 | 基础 API |
| RGON | `3113y/REPGON_Docs-Trans-zh_cn` 保留的旧文档快照 | REP 覆盖层 |
| RGON+ | TeamREPENTOGON 官方仓库 `docs/` | REP+ 覆盖层 |
| EID | `wofsauge/External-Item-Descriptions` 的 API 与源码资料 | 独立可选命名空间 |

每次导入记录仓库地址、分支、提交号、文件路径与抓取时间。RGON / RGON+ 同名 API 必须以文档或变更记录为证据标记为 `override`，不能只按名称推测。EID 不覆盖原版命名空间；其依赖 RGON 的功能应标记相应前置条件。

环境解析顺序：

1. 选择基础版本 `rep` 或 `rep+`。
2. 启用 `rgon` 或 `rgon+` 时，应用对应覆盖与扩展。
3. 启用 `eid` 时，追加独立 EID API；其依赖 RGON 的成员只在对应环境内有效。
4. 明确查询不兼容 API 时，返回页面与所需环境说明；默认结果只包含当前环境可直接使用的 API。

## 规范化条目

示意：

```yaml
id: vanilla.entity_player.add_hearts
signature: "EntityPlayer:AddHearts(amount)"
kind: method
variants:
  - environment: { game: rep, dependencies: [] }
    relation: base
    source:
      repository_url: "canonical upstream repository URL"
      revision: "immutable source commit SHA"
      source_path: "path to the upstream documentation file"
    description:
      en: "Upstream English text"
      zh: "LLM 中文译文"
      origin: translated
  - environment: { game: rep, dependencies: [rgon] }
    relation: override
    overrides: vanilla.entity_player.add_hearts
    source:
      repository_url: "https://github.com/3113y/REPGON_Docs-Trans-zh_cn"
      revision: "immutable source commit SHA"
      source_path: "path to the RGON documentation file"
```

固定保存英文原文、签名、参数、返回值、枚举值、版本与来源。不得通过翻译或推断改写这些事实。

描述来源字段：

- `upstream`：上游原始英文。
- `translated`：现有上游描述的中文 LLM 翻译。
- `inferred`：上游未提供描述时生成的英/中文解释。
- `community_corrected`：社区合并的修正，保留修改记录和依据。

`inferred` 描述仅可依据签名、参数、所属类型和相邻 API 生成，并记录推断依据。页面与 MCP 先显示描述正文，再在末尾附提示：

```text
中文：LLM 智能推断说明：上游文档未提供此描述。
EN: LLM-inferred description: no upstream description was provided.
```

已有上游描述的译文不要求逐条人工复审，但翻译必须使用统一术语表，保护 API 标识符、代码块、链接和 Markdown 结构。

## 翻译与推断流水线

1. 从固定上游版本提取 Markdown、签名与元数据。
2. 规范化为 API 条目并保留原文。
3. 对已有描述运行多 Agent 翻译和术语一致性检查。
4. 对缺失描述运行受限提示词的英文、中文推断生成。
5. 校验签名、参数、链接、双语配对、环境归属和 Markdown。

模型不能新增 API 或修改签名。解析、翻译或推断失败时，英文原文与结构化 API 信息仍可发布；失败内容不得伪装为翻译。

## MCP

MCP 无状态，每次调用显式传入环境：

```text
wiki_search(query, game, dependencies, language, category?, include_incompatible=false)
wiki_read(page, game, dependencies, language, include_incompatible=false)
wiki_list(game?, dependencies?, language?, category?)
wiki_stats()
```

`language` 取值为 `zh`、`en` 或 `auto`。调用 Agent 应按最终用户 prompt 选择语言；服务端无法读取该 prompt。若未明确指定，`auto` 仅能基于查询文本作保守判断。返回内容始终保留 API 签名、来源与环境标签。

## GitHub Pages 文档站

新建单独的静态站仓库，主仓库生成并验证文档产物后再推送过去。站点使用与参考站相近的 Material 风格：顶部全局导航、搜索、环境选择器和语言切换；左侧树形 API 导航；右侧页内目录。

静态页面分别发布在：

```text
/zh/{page-path}  中文译文或中文推断说明
/en/{page-path}  英文原文或英文推断说明
```

右上角语言切换为 `中文 / EN`，应保留当前页面和环境选择。环境选择器提供基础版本 `REP / REP+` 与依赖开关 `RGON` / `RGON+`、`EID`；RGON 与基础版本自动约束。不可用 API 不隐藏，而以兼容性提示显示。页面还显示签名、适用环境、RGON 覆盖关系、来源以及推断提示。

## 社区纠正

GitHub Pages 仓库只存生成产物，不接收内容修改。每个站点页面提供“纠正此描述”链接，指向主仓库中对应条目的预填充 Issue 或 Pull Request。

用户可纠正中文译文、LLM 推断说明与上游勘误。上游英文原文不可改写；发现上游错误时以附加的社区勘误保存。README 必须说明：条目定位方法、允许和禁止修改的字段、翻译/推断/勘误的贡献示例、Pull Request 所需依据及受影响环境。

自动检查确保签名未变、Markdown 有效、术语一致且环境信息完整。合并的社区修正使用 `community_corrected` 标记并保留历史。

## 同步、发布与验证

上游同步采用显式命令或 CI 工作流，仅重新处理源文件变化的页面；英文原文未变化时复用既有翻译。上游不可访问或结构变化时保留上一次成功数据，不发布空白或不完整站点。

MCP 包与 GitHub Pages 默认每周发布一次，而不是每次修正合并即发布。每个发布版本包含变更摘要、来源版本、上次发布时间与受影响环境。保留人工提前发布通道，仅用于重大上游 API 变更或明显误导性内容的紧急修正。

每次构建验证：

- 签名和版本事实可回链到上游。
- 中英文页面可配对，链接完整。
- 环境解析与 RGON 覆盖规则符合快照测试。
- 静态站可以完整构建。
- MCP 文档版本与站点版本一致。
