# AI Agent

目标：理解 Agent 的模型、状态、工具、记忆、控制流和人机协同，并能判断何时不该使用 Agent。

- [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction) — 从 Agent 原理、框架到 Agentic RAG 与评估。`英文` `免费` `核验：2026-09-07`
- [LangGraph Documentation](https://docs.langchain.com/oss/python/langgraph/overview) — 有状态、可持久化、支持人工介入的 Agent 编排。`英文` `免费` `核验：2026-09-07`
- [LlamaIndex Agents](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/) — 面向数据与工具的 Agent 设计。`英文` `免费` `核验：2026-09-07`
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/) — 微软官方多智能体与工作流开发框架文档。`英文` `免费` `核验：2026-09-07`
- [Model Context Protocol](https://modelcontextprotocol.io/) — 模型连接外部工具和数据源的开放协议。`英文` `免费` `核验：2026-09-07`
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) — 工具、Handoff、Guardrail、Session 与 Trace 的轻量 SDK。`英文` `免费` `核验：2026-09-07`

## 选型提醒

如果任务路径稳定、规则明确且风险高，优先使用确定性工作流；只有在步骤无法预先穷举、需要动态判断时，才增加 Agent 自主性。工具调用必须配套最小权限、超时、幂等、审批和回滚。
