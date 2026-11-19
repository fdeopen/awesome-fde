# 评测数据约定

每条样本包含 sample_id、输入、身份、期望证据、期望行为、分层、标注人、许可和数据集版本。开发集与盲测集分开；按时间或主体切分，避免同一文档的改写泄漏到两组。

1. 先运行[离线练习](../../cookbook/examples/README.md)，理解断言与失败原因。
2. 用[Golden Dataset](../templates/golden-dataset.md)登记数据。
3. 分别提交[Agent评测](../templates/agent-evaluation.md)与[RAG评测](../templates/rag-evaluation.md)，保留逐题结果。
4. 用[Bad Case](../templates/bad-case.md)跟踪根因与回归。

不能把小样本100%通过外推到生产。目标阈值、样本覆盖、人工一致性和未验证能力必须同时报告。
