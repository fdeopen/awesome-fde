# 向量数据库

向量数据库是检索系统组件，不是知识库效果的替代指标。先验证解析、切分、Embedding、检索、重排和权限策略，再决定是否需要独立向量数据库。

| 项目 | 典型定位 | 评估重点 | 官方入口 |
| --- | --- | --- | --- |
| pgvector | 在 PostgreSQL 内增加向量检索 | 适合已有 Postgres 团队；关注索引、过滤和规模边界 | [GitHub](https://github.com/pgvector/pgvector) |
| Qdrant | 专用向量搜索引擎 | Payload 过滤、分片、备份与多租户 | [GitHub](https://github.com/qdrant/qdrant) · [文档](https://qdrant.tech/documentation/) |
| Milvus | 分布式向量数据库 | 大规模检索、资源规划、运维与一致性 | [GitHub](https://github.com/milvus-io/milvus) · [文档](https://milvus.io/docs) |
| Weaviate | 向量数据库与混合检索 | Schema、过滤、模块、备份与集群 | [GitHub](https://github.com/weaviate/weaviate) · [文档](https://docs.weaviate.io/weaviate) |
| Elasticsearch | 文本、向量与混合检索 | 现有搜索栈复用、授权、资源与相关性调优 | [文档](https://www.elastic.co/guide/en/elasticsearch/reference/current/knn-search.html) |

`核验：2026-09-07`。

## 压测建议

- 使用真实查询分布和权限过滤条件，而非只测裸向量 Top-K。
- 同时报告 Recall@K、NDCG/MRR、P95 延迟、索引时间、容量和成本。
- 验证新增、更新、删除、重建索引和灾备恢复。
- 对比“数据库内混合检索”和“应用层拼接”对质量与复杂度的影响。
