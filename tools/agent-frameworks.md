# Agent 框架

选择框架时，优先看状态、控制流、持久化、人工介入、Trace、评估和部署能力，不要只比较示例数量。

| 项目 | 核心特点 | 适合场景 | 官方入口 |
| --- | --- | --- | --- |
| LangGraph | 图式状态机、持久化、人工介入 | 需要显式控制和长任务状态的 Agent | [GitHub](https://github.com/langchain-ai/langgraph) · [文档](https://docs.langchain.com/oss/python/langgraph/overview) |
| LlamaIndex | 数据连接、索引、检索与 Agent | 数据密集型 Agent 与 RAG | [GitHub](https://github.com/run-llama/llama_index) · [文档](https://docs.llamaindex.ai/) |
| Microsoft Agent Framework | Agent、工作流与企业集成 | 微软技术栈及多智能体编排 | [GitHub](https://github.com/microsoft/agent-framework) · [文档](https://learn.microsoft.com/en-us/agent-framework/) |
| OpenAI Agents SDK | Tool、Handoff、Guardrail、Session、Trace | 轻量多 Agent 与工具调用 | [GitHub](https://github.com/openai/openai-agents-python) · [文档](https://openai.github.io/openai-agents-python/) |
| Pydantic AI | 类型安全、依赖注入与结构化输出 | Python 服务和强 Schema 应用 | [GitHub](https://github.com/pydantic/pydantic-ai) · [文档](https://ai.pydantic.dev/) |
| CrewAI | Role/Task/Crew 抽象与流程编排 | 角色化多 Agent 原型 | [GitHub](https://github.com/crewAIInc/crewAI) · [文档](https://docs.crewai.com/) |

`核验：2026-09-07`。

## 选型红线

- 无法固定或记录模型、Prompt、工具和知识版本
- 工具调用缺少权限、超时、幂等、审批或回滚
- 运行状态只存在聊天文本中，不能恢复或审计
- 无法导出 Trace、评估数据和关键业务结果
- 框架升级会强制迁移且没有清晰退出路径
