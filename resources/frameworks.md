# 企业AI技术资源图谱

重点项目逐条记录仓库、文档、定位、适用场景、技术特征、许可和企业注意事项。元数据核验不等于部署或安全认证。

## 工程层导航

| 工程层 | 入口 |
| --- | --- |
| 大模型与推理 | [进入](../tools/model-serving.md) |
| Prompt与上下文 | [进入](prompt-and-context.md) |
| Agent框架与Workflow | [进入](../cookbook/agent/README.md) |
| Agent Harness | [进入](../cookbook/harness/README.md) |
| Multi-Agent | [进入](../cookbook/multi-agent/README.md) |
| Skill | [进入](../cookbook/skill/README.md) |
| MCP | [进入](../cookbook/mcp/README.md) |
| RAG与知识库 | [进入](rag-and-knowledge.md) |
| 文档解析 | [进入](rag-and-knowledge.md) |
| 数据清洗与治理 | [进入](../toolkit/templates/data-governance.md) |
| 向量数据库 | [进入](../tools/vector-databases.md) |
| 知识图谱与本体 | [进入](../cookbook/ontology/README.md) |
| 企业系统集成 | [进入](../delivery/implementation.md) |
| AI评测 | [进入](llmops-and-evaluation.md) |
| 可观测性 | [进入](../tools/observability.md) |
| 模型部署 | [进入](model-deployment.md) |
| AI安全与治理 | [进入](ai-security.md) |
| 企业级AI应用 | [进入](../tools/application-platforms.md) |
| Vibe Coding | [进入](../cookbook/llm/README.md) |
| 模型网关 | [进入](../tools/ai-gateways.md) |

## vllm

- 分类：大模型与推理服务
- 官方仓库：[GitHub](https://github.com/vllm-project/vllm)
- 官方文档：[文档](https://docs.vllm.ai/)
- 核心定位：批处理推理服务
- 适用场景：大模型与推理服务相关交付
- 技术特点：批处理推理服务
- 许可证：Apache-2.0；[仓库许可说明](https://github.com/vllm-project/vllm?tab=readme-ov-file#license)
- 企业注意事项：需要 GPU 容量与模型兼容性验证
- 核验：2026-11-19；GitHub公开API确认仓库存在、规范地址和许可证元数据；文档可达性见外链报告

## llama.cpp

- 分类：本地推理
- 官方仓库：[GitHub](https://github.com/ggml-org/llama.cpp)
- 官方文档：[文档](https://github.com/ggml-org/llama.cpp/tree/master/docs)
- 核心定位：GGUF 与多硬件后端
- 适用场景：本地推理相关交付
- 技术特点：GGUF 与多硬件后端
- 许可证：MIT；[仓库许可说明](https://github.com/ggml-org/llama.cpp?tab=readme-ov-file#license)
- 企业注意事项：模型权重许可独立于引擎
- 核验：2026-11-19；GitHub公开API确认仓库存在、规范地址和许可证元数据；文档可达性见外链报告

## langgraph

- 分类：Agent Workflow
- 官方仓库：[GitHub](https://github.com/langchain-ai/langgraph)
- 官方文档：[文档](https://docs.langchain.com/oss/python/langgraph/overview)
- 核心定位：显式状态与持久化编排
- 适用场景：Agent Workflow相关交付
- 技术特点：显式状态与持久化编排
- 许可证：MIT；[仓库许可说明](https://github.com/langchain-ai/langgraph?tab=readme-ov-file#license)
- 企业注意事项：自行设计业务幂等和恢复策略
- 核验：2026-11-19；GitHub公开API确认仓库存在、规范地址和许可证元数据；文档可达性见外链报告

## deepagents

- 分类：Agent Harness
- 官方仓库：[GitHub](https://github.com/langchain-ai/deepagents)
- 官方文档：[文档](https://docs.langchain.com/oss/python/deepagents/overview)
- 核心定位：任务规划与文件系统工具
- 适用场景：Agent Harness相关交付
- 技术特点：任务规划与文件系统工具
- 许可证：MIT；[仓库许可说明](https://github.com/langchain-ai/deepagents?tab=readme-ov-file#license)
- 企业注意事项：沙箱和长任务预算须单独约束
- 核验：2026-11-19；GitHub公开API确认仓库存在、规范地址和许可证元数据；文档可达性见外链报告

## skills

- 分类：Skill
- 官方仓库：[GitHub](https://github.com/anthropics/skills)
- 官方文档：[文档](https://github.com/anthropics/skills)
- 核心定位：文件化技能示例
- 适用场景：Skill相关交付
- 技术特点：文件化技能示例
- 许可证：按各Skill目录声明；根目录未发现统一LICENSE；[仓库许可说明](https://github.com/anthropics/skills)
- 企业注意事项：逐目录许可；示例不可直接获得生产权限
- 核验：2026-11-19；GitHub公开API确认仓库存在、规范地址和许可证元数据；文档可达性见外链报告；已检查根目录许可文件/文件清单

## python-sdk

- 分类：MCP
- 官方仓库：[GitHub](https://github.com/modelcontextprotocol/python-sdk)
- 官方文档：[文档](https://modelcontextprotocol.io/)
- 核心定位：工具与资源协议 SDK
- 适用场景：MCP相关交付
- 技术特点：工具与资源协议 SDK
- 许可证：MIT；[仓库许可说明](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#license)
- 企业注意事项：协议连接不等于用户授权
- 核验：2026-11-19；GitHub公开API确认仓库存在、规范地址和许可证元数据；文档可达性见外链报告

## ragflow

- 分类：RAG与知识库
- 官方仓库：[GitHub](https://github.com/infiniflow/ragflow)
- 官方文档：[文档](https://ragflow.io/docs/)
- 核心定位：文档解析与检索工作流
- 适用场景：RAG与知识库相关交付
- 技术特点：文档解析与检索工作流
- 许可证：Apache-2.0；[仓库许可说明](https://github.com/infiniflow/ragflow?tab=readme-ov-file#license)
- 企业注意事项：验证解析、隔离与资源开销
- 核验：2026-11-19；GitHub公开API确认仓库存在、规范地址和许可证元数据；文档可达性见外链报告

## docling

- 分类：文档解析
- 官方仓库：[GitHub](https://github.com/docling-project/docling)
- 官方文档：[文档](https://docling-project.github.io/docling/)
- 核心定位：结构化文档转换
- 适用场景：文档解析相关交付
- 技术特点：结构化文档转换
- 许可证：MIT；[仓库许可说明](https://github.com/docling-project/docling?tab=readme-ov-file#license)
- 企业注意事项：解析模型和第三方依赖单独核验
- 核验：2026-11-19；GitHub公开API确认仓库存在、规范地址和许可证元数据；文档可达性见外链报告

## great_expectations

- 分类：数据清洗与治理
- 官方仓库：[GitHub](https://github.com/fivetran/great_expectations)
- 官方文档：[文档](https://docs.greatexpectations.io/docs/)
- 核心定位：数据质量断言
- 适用场景：数据清洗与治理相关交付
- 技术特点：数据质量断言
- 许可证：Apache-2.0；[仓库许可说明](https://github.com/fivetran/great_expectations?tab=readme-ov-file#license)
- 企业注意事项：断言需要业务口径与数据责任人
- 核验：2026-11-19；GitHub公开API确认仓库存在、规范地址和许可证元数据；文档可达性见外链报告

## qdrant

- 分类：向量数据库
- 官方仓库：[GitHub](https://github.com/qdrant/qdrant)
- 官方文档：[文档](https://qdrant.tech/documentation/)
- 核心定位：向量检索与过滤
- 适用场景：向量数据库相关交付
- 技术特点：向量检索与过滤
- 许可证：Apache-2.0；[仓库许可说明](https://github.com/qdrant/qdrant?tab=readme-ov-file#license)
- 企业注意事项：检查租户过滤和删除传播
- 核验：2026-11-19；GitHub公开API确认仓库存在、规范地址和许可证元数据；文档可达性见外链报告

## rdflib

- 分类：知识图谱与本体
- 官方仓库：[GitHub](https://github.com/RDFLib/rdflib)
- 官方文档：[文档](https://rdflib.readthedocs.io/)
- 核心定位：RDF 图读写与查询
- 适用场景：知识图谱与本体相关交付
- 技术特点：RDF 图读写与查询
- 许可证：BSD-3-Clause；[仓库许可说明](https://github.com/RDFLib/rdflib?tab=readme-ov-file#license)
- 企业注意事项：业务对象与主数据映射需人工确定
- 核验：2026-11-19；GitHub公开API确认仓库存在、规范地址和许可证元数据；文档可达性见外链报告

## n8n

- 分类：企业系统集成
- 官方仓库：[GitHub](https://github.com/n8n-io/n8n)
- 官方文档：[文档](https://docs.n8n.io/)
- 核心定位：连接器与工作流
- 适用场景：企业系统集成相关交付
- 技术特点：连接器与工作流
- 许可证：Sustainable Use License；企业文件适用Enterprise License；[仓库许可说明](https://github.com/n8n-io/n8n/blob/master/LICENSE.md)
- 企业注意事项：source-available；商业托管需核对条款
- 核验：2026-11-19；GitHub公开API确认仓库存在、规范地址和许可证元数据；文档可达性见外链报告；已检查根目录许可文件/文件清单

## ragas

- 分类：AI评测
- 官方仓库：[GitHub](https://github.com/vibrantlabsai/ragas)
- 官方文档：[文档](https://docs.ragas.io/)
- 核心定位：RAG质量与评估流程
- 适用场景：AI评测相关交付
- 技术特点：RAG质量与评估流程
- 许可证：Apache-2.0；[仓库许可说明](https://github.com/vibrantlabsai/ragas?tab=readme-ov-file#license)
- 企业注意事项：模型评分需要人工校准
- 核验：2026-11-19；GitHub公开API确认仓库存在、规范地址和许可证元数据；文档可达性见外链报告

## langfuse

- 分类：可观测性
- 官方仓库：[GitHub](https://github.com/langfuse/langfuse)
- 官方文档：[文档](https://langfuse.com/docs)
- 核心定位：Trace、数据集和成本
- 适用场景：可观测性相关交付
- 技术特点：Trace、数据集和成本
- 许可证：MIT（非企业目录）；企业目录适用ee/LICENSE；[仓库许可说明](https://github.com/langfuse/langfuse/blob/main/LICENSE)
- 企业注意事项：企业功能许可及日志敏感数据需核验
- 核验：2026-11-19；GitHub公开API确认仓库存在、规范地址和许可证元数据；文档可达性见外链报告；已检查根目录许可文件/文件清单

## dify

- 分类：企业级AI应用
- 官方仓库：[GitHub](https://github.com/langgenius/dify)
- 官方文档：[文档](https://docs.dify.ai/)
- 核心定位：可视化应用与知识工作流
- 适用场景：企业级AI应用相关交付
- 技术特点：可视化应用与知识工作流
- 许可证：Dify License（Apache-2.0加多租户与品牌限制）；[仓库许可说明](https://github.com/langgenius/dify/blob/main/LICENSE)
- 企业注意事项：自定义许可；多租户与品牌条款需核对
- 核验：2026-11-19；GitHub公开API确认仓库存在、规范地址和许可证元数据；文档可达性见外链报告；已检查根目录许可文件/文件清单

## aider

- 分类：Vibe Coding
- 官方仓库：[GitHub](https://github.com/Aider-AI/aider)
- 官方文档：[文档](https://aider.chat/docs/)
- 核心定位：终端 AI 编程
- 适用场景：Vibe Coding相关交付
- 技术特点：终端 AI 编程
- 许可证：Apache-2.0；[仓库许可说明](https://github.com/Aider-AI/aider?tab=readme-ov-file#license)
- 企业注意事项：生成代码需测试并检查依赖
- 核验：2026-11-19；GitHub公开API确认仓库存在、规范地址和许可证元数据；文档可达性见外链报告

## promptfoo

- 分类：AI安全与治理
- 官方仓库：[GitHub](https://github.com/promptfoo/promptfoo)
- 官方文档：[文档](https://www.promptfoo.dev/docs/intro/)
- 核心定位：提示评估与红队测试
- 适用场景：AI安全与治理相关交付
- 技术特点：提示评估与红队测试
- 许可证：MIT；[仓库许可说明](https://github.com/promptfoo/promptfoo?tab=readme-ov-file#license)
- 企业注意事项：在隔离环境运行对抗测试
- 核验：2026-11-19；GitHub公开API确认仓库存在、规范地址和许可证元数据；文档可达性见外链报告

## litellm

- 分类：模型网关
- 官方仓库：[GitHub](https://github.com/BerriAI/litellm)
- 官方文档：[文档](https://docs.litellm.ai/docs/)
- 核心定位：统一模型调用与预算
- 适用场景：模型网关相关交付
- 技术特点：统一模型调用与预算
- 许可证：MIT（非enterprise目录）；企业目录适用独立许可；[仓库许可说明](https://github.com/BerriAI/litellm/blob/main/LICENSE)
- 企业注意事项：网关权限不能代替业务权限
- 核验：2026-11-19；GitHub公开API确认仓库存在、规范地址和许可证元数据；文档可达性见外链报告；已检查根目录许可文件/文件清单

## mlflow

- 分类：模型部署与生命周期
- 官方仓库：[GitHub](https://github.com/mlflow/mlflow)
- 官方文档：[文档](https://mlflow.org/docs/latest/)
- 核心定位：实验跟踪与模型管理
- 适用场景：模型部署与生命周期相关交付
- 技术特点：实验跟踪与模型管理
- 许可证：Apache-2.0；[仓库许可说明](https://github.com/mlflow/mlflow?tab=readme-ov-file#license)
- 企业注意事项：部署与存储访问控制由团队配置
- 核验：2026-11-19；GitHub公开API确认仓库存在、规范地址和许可证元数据；文档可达性见外链报告

## CrewAI

- 分类：Multi-Agent
- 官方仓库：[GitHub](https://github.com/crewAIInc/crewAI)
- 官方文档：[文档](https://docs.crewai.com/)
- 核心定位：角色与任务协作
- 适用场景：可拆分的研究与审阅工作流
- 技术特点：角色、任务与流程编排
- 许可证：MIT；[仓库许可说明](https://github.com/crewAIInc/crewAI?tab=readme-ov-file#license)
- 企业注意事项：先对比单工作流成本；交接不能代替事实核查
- 核验：2026-11-19；GitHub公开API核验

## 部署地区与采购判断

大陆企业应实测模型和依赖下载可用性、私有化硬件资源、日志位置及数据出域路径。框架开源许可不涵盖模型权重和商业托管服务。按[选型矩阵](../toolkit/templates/technology-selection.md)记录结果。
