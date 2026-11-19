# FDE Toolkit · 工程交付工具箱

30 项任务模板覆盖发现、方案、PoC、工程、验收与价值复盘。其中5项复用历史模板并增补使用示例，25项为新增底稿；原模板库其余8项继续可用。

## 按任务选择

| 阶段 | 模板 | 使用重点 |
| --- | --- | --- |
| 1 | [企业AI业务访谈提纲](../templates/discovery/interview-guide.md) | 先观察一次任务，再访谈决策人；至少保存一条反对立项的证据。 |
| 2 | [企业AI需求调研表](templates/requirements.md) | 逐需求写触发、输入输出及可检验条件；把愿望和事实分栏记录。 |
| 2 | [企业AI成熟度评估](templates/maturity.md) | 用0无证据、1人工可做、2有规范、3可重复、4可审计评分；每分绑定证据，不用均分掩盖阻断项。 |
| 3 | [AI场景发现清单](templates/scenario-discovery.md) | 沿触发、等待、判断、交接、异常扫描流程，先比较规则和流程改造。 |
| 3 | [AI场景评分矩阵](templates/scenario-score.md) | 先检查数据授权、结果责任和停止条件；阻断项不参与排名。分数用于相对排序，不是ROI。 |
| 3 | [AI项目优先级评估](templates/priority.md) | 在评分基础上加入资源冲突、先后依赖与机会成本；保留暂缓项目的重启条件。 |
| 5 | [系统与数据资产盘点](templates/system-data.md) | 逐系统核对主键、服务账号、更新频率、地域与删除链路，凭据只记录保管位置。 |
| 2 | [业务流程分析](templates/process-map.md) | 分别画As-Is与To-Be，标记每一步的系统、责任、等待和回退。 |
| 4 | [业务对象与本体建模](templates/ontology.md) | 先统一业务术语和主键，再定义关系、规则与动作；本体不等同于向量索引。 |
| 6 | [技术选型评估矩阵](templates/technology-selection.md) | 在相同数据、硬件和权限条件下比较；记录否决条件与替换成本。 |
| 6 | [AI解决方案设计](templates/solution.md) | 关联ADR、数据目录和需求ID；每个组件解释它解决的约束。 |
| 7 | [PoC项目计划书](../templates/poc/poc-charter.md) | 预先冻结样本和阈值，分离开发集与盲测集；保留失败结论。 |
| 7 | [PoC验收标准](templates/poc-acceptance.md) | 所有阈值为项目协商值；将业务、质量、风险和成本分别判定，风险不被平均分抵消。 |
| 8 | [RAG知识库建设方案](templates/rag-design.md) | 先用小样本核查解析与ACL，再调切分、检索和重排；避免只优化最终回答。 |
| 8 | [Agent设计说明书](templates/agent-design.md) | 绘制状态转移并测试失败路径；动作执行前检查授权和幂等键。 |
| 8 | [Skill设计模板](templates/skill-design.md) | 明确何时触发与何时不适用；技能文本不能替代运行环境的权限控制。 |
| 8 | [MCP接口设计](templates/mcp-interface.md) | 协议版本与SDK固定后再实现；先定义稳定错误码、授权与超时，再连接模型。 |
| 5 | [企业AI数据治理方案](templates/data-governance.md) | 逐数据集明确用途、授权、保留和删除；把质量规则变成可运行断言。 |
| 9 | [Golden Dataset模板](templates/golden-dataset.md) | 记录判定依据而非只有参考答案；变更样本需新版本，禁止把盲测样本加入Prompt调优。 |
| 9 | [Bad Case记录](templates/bad-case.md) | 记录最小可复现输入、Trace与业务影响；分清模型、数据、工具、流程和权限原因。 |
| 9 | [Agent评测报告](templates/agent-evaluation.md) | 不能只看最终文本；同时断言工具参数、状态、审批和副作用。 |
| 9 | [RAG评测报告](templates/rag-evaluation.md) | 报告分母和逐题证据；模型Judge分数只能作为辅助信号。 |
| 6 | [AI项目风险清单](templates/risk-register.md) | 风险评分用于排序；指定检测、响应和恢复负责人，不只列出风险名称。 |
| 10 | [AI安全治理清单](templates/security-governance.md) | 用测试证据支持每一项；未通过的项目记录补偿措施和风险接受人。 |
| 8 | [项目实施计划](../templates/implementation/project-plan.md) | 每个里程碑绑定退出标准，范围变更同步影响评测与交接。 |
| 10 | [上线检查清单](../templates/acceptance/launch-gate.md) | 在测试环境演练供应商故障与回退；未完成四道门不扩大流量。 |
| 10 | [运维交接模板](templates/handover.md) | 让接收团队独立完成一次恢复演练；文档签收不等于可运行交接。 |
| 6 | [AI项目报价模板](templates/quotation.md) | 此表是估算底稿，不构成合同；区分税费、含量上限、维护与第三方成本。 |
| 11 | [ROI测算模板](templates/roi.md) | 公式见计算器；分别列工时改善与可兑现收益，做低/中/高敏感性分析。 |
| 12 | [项目复盘与资产沉淀](../templates/retrospective/project-retrospective.md) | 用第二次复用检验资产价值；保留失败假设和停止决策。 |

## 实用工具

- [交付检查单](checklists/README.md)：从PoC到上线的证据核验。
- [评测数据约定](evaluation/README.md)：样本、版本、评分与失败记录。
- [工作提示词](prompts/README.md)：访谈归纳、方案审阅与复盘。
- [ROI计算器](calculators/README.md)：离线算例与敏感性分析。
- [原13份模板](../templates/README.md)：RACI、ADR、审计索引、供应商尽调与运营复盘。

阶段定义见 [Playbook](../playbook/README.md)，技术方法见 [Cookbook](../cookbook/README.md)，生态入口见 [社区](../community/README.md)。
