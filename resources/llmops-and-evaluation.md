# 评测、可观测与 LLMOps

目标：把“看起来不错”升级为版本化任务集、质量门禁、线上反馈和持续回归。

- [OpenAI Evals](https://github.com/openai/evals) — 构建和运行模型评估的开源框架。`英文` `免费` `核验：2026-09-07`
- [Ragas Documentation](https://docs.ragas.io/) — RAG 与 LLM 应用评估。`英文` `免费` `核验：2026-09-07`
- [Langfuse Documentation](https://langfuse.com/docs) — Trace、评估、数据集、Prompt 与成本管理。`英文` `免费/商业版` `核验：2026-09-07`
- [MLflow GenAI](https://mlflow.org/docs/latest/genai/) — 生成式 AI 的追踪、评估与生命周期管理。`英文` `免费` `核验：2026-09-07`
- [Arize Phoenix](https://arize.com/docs/phoenix) — LLM Trace、评估与可观测。`英文` `免费/商业版` `核验：2026-09-07`
- [OpenTelemetry Documentation](https://opentelemetry.io/docs/) — Trace、Metric 与 Log 的开放标准。`英文` `免费` `核验：2026-09-07`
- [agent-qa：验证编码代理的应用变更](https://vostride.com/docs/agent-qa/guides/coding-agent-workflow) — 面向交付 AI 应用的工程团队，用运行与步骤证据诊断失败并定向重跑；需运行待测应用，模型调用费用随配置和用量变化。`英文` `免费文档` `核验：2026-10-31`

## 五层评估

| 层级 | 关注点 |
| --- | --- |
| 任务 | 答案、抽取、分类或行动是否正确 |
| 流程 | 是否在正确步骤调用正确工具并保留审批 |
| 系统 | 延迟、可用性、容量、恢复和成本 |
| 风险 | 注入、越权、泄露、误导、偏差和不可审计行为 |
| 业务 | 周期、质量、收入、成本、风险暴露和用户采用 |

评估集、生产数据和训练/优化数据应明确隔离。新增失败样本进入回归集，但也要持续加入新分布样本。
