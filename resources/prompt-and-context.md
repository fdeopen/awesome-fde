# Prompt 与上下文工程

目标：把自然语言指令升级为可版本化、可评估、可维护的系统组件。

- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) — 官方 Prompt 设计与模型协作方法。`英文` `免费` `核验：2026-09-07`
- [Anthropic Prompt Engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) — 从成功标准、测试到提示改进的官方指南。`英文` `免费` `核验：2026-09-07`
- [Google Prompt Design Strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies) — Gemini 官方提示策略与示例。`英文` `免费` `核验：2026-09-07`
- [Prompt Engineering Guide](https://www.promptingguide.ai/zh) — 汇总常见提示方法、模型与研究资料。`中文` `免费` `核验：2026-09-07`
- [Hugging Face Context Engineering Course](https://huggingface.co/learn/context-course/unit0/introduction) — 面向 Agent 的上下文组织课程。`英文` `免费` `核验：2026-09-07`

## 生产化检查

- Prompt 有版本、负责人、输入 Schema、输出 Schema 和变更记录。
- 评估集覆盖高频、长尾、高风险与对抗输入。
- 不在 Prompt 中硬编码密钥、客户机密或不可审计的权限规则。
- Prompt 变更与模型、知识源、工具变更一样进入回归测试。
