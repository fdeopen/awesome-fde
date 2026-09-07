# RAG 与企业知识库

目标：建立从数据接入、解析、切分、索引、检索、重排到引用与权限过滤的可评估链路。

- [LangChain Retrieval](https://docs.langchain.com/oss/python/langchain/retrieval) — RAG 组件、检索流程与常见架构。`英文` `免费` `核验：2026-09-07`
- [LlamaIndex Documentation](https://docs.llamaindex.ai/) — 数据连接、索引、检索和 Agent 应用框架。`英文` `免费` `核验：2026-09-07`
- [RAGFlow](https://github.com/infiniflow/ragflow) — 面向复杂文档理解和可视化工作流的开源 RAG 引擎。`中英` `免费` `核验：2026-09-07`
- [Docling](https://docling-project.github.io/docling/) — 面向 PDF、Office 与网页的开源文档转换工具。`英文` `免费` `核验：2026-09-07`
- [Unstructured Documentation](https://docs.unstructured.io/) — 文档解析、分块与数据预处理。`英文` `免费/商业版` `核验：2026-09-07`
- [Qdrant Documentation](https://qdrant.tech/documentation/) — 向量搜索、过滤与生产部署。`英文` `免费/商业版` `核验：2026-09-07`

## 生产化检查

- 权限过滤在检索阶段生效，而不是生成答案后再遮盖。
- 每条答案可追溯到知识源、版本和片段。
- 评估拆分检索质量与生成质量，避免只看最终回答。
- 建立增量更新、删除、过期、冲突和失败文档处理机制。
- 记录无答案、低置信度和转人工路径。
