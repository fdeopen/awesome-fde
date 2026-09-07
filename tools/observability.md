# 评测与可观测工具

| 项目 | 主要能力 | 评估重点 | 官方入口 |
| --- | --- | --- | --- |
| Langfuse | Trace、数据集、评估、Prompt 和成本 | 自托管、数据保留、采样和业务指标关联 | [GitHub](https://github.com/langfuse/langfuse) · [文档](https://langfuse.com/docs) |
| MLflow | 实验、模型与生成式 AI 追踪评估 | 现有 ML 平台整合、评估扩展和权限 | [GitHub](https://github.com/mlflow/mlflow) · [文档](https://mlflow.org/docs/latest/genai/) |
| Arize Phoenix | OpenTelemetry Trace 与 LLM 评估 | 数据规模、评估器、部署和保留策略 | [GitHub](https://github.com/Arize-ai/phoenix) · [文档](https://arize.com/docs/phoenix) |
| Ragas | RAG/Agent 数据集与评估 | 指标适用性、Judge 偏差和人工校准 | [GitHub](https://github.com/explodinggradients/ragas) · [文档](https://docs.ragas.io/) |
| OpenTelemetry | Trace、Metric、Log 开放标准 | 语义约定、采样、脱敏和后端兼容 | [GitHub](https://github.com/open-telemetry) · [文档](https://opentelemetry.io/docs/) |

`核验：2026-09-07`。

不要把“记录所有 Prompt”误认为可观测。生产系统需要在可重建决策链与数据最小化之间取得平衡，并把技术 Trace 连接到用户反馈、业务结果、变更和事故。
