# FDE Cookbook · 工程实践

10份配方强调输入、步骤、失败路径和验收。它们是架构与练习指南；具体SDK用法以[已核验技术图谱](../resources/frameworks.md)中的官方文档为准。

| 配方 | 练习问题 |
| --- | --- |
| [模型调用与快速原型](llm/README.md) | 从一份询价文本提取产品、数量和交期 |
| [权限感知RAG](rag/README.md) | 为售后政策生成带证据的答复 |
| [受控工具Agent](agent/README.md) | 检索订单状态并生成处理建议 |
| [多智能体协作](multi-agent/README.md) | 分析员提出方案，审阅员检查证据 |
| [可复用Skill](skill/README.md) | 将知识清理流程打包为团队能力 |
| [MCP工具接入](mcp/README.md) | 提供只读订单查询工具 |
| [长任务Harness](harness/README.md) | 让文档处理任务中断后继续 |
| [业务本体驱动查询](ontology/README.md) | 把订单、物料、条款和动作统一起来 |
| [可回归的工程评测](evaluation/README.md) | 发现版本升级造成的质量回退 |
| [从影子运行到生产](deployment/README.md) | 把评测通过的版本交给运营 |

## 先运行一个离线闭环

[离线交付练习](examples/README.md)不需要API密钥，提供合成知识、权限过滤、引用、弃答、工具幂等与评测断言。它是基础工程参考实现，不模拟大模型智能，也不声称生产就绪。

练习完成后，将输出写入[Toolkit](../toolkit/README.md)，按[Playbook](../playbook/README.md)推进，并通过[社区](../community/README.md)提交改进。
