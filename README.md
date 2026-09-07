# Awesome FDE

> 面向 FDE（Forward Deployed Engineer，前线部署工程师）与企业 AI 实践者的中文精选资源库：从理解岗位，到把大模型、Agent、RAG 与 AI Infra 交付进真实业务。

[FDEChina.ai](https://fdechina.ai/) · [FDE Guide](https://github.com/bingyue/fde-guide) · [FDE Skills](https://github.com/bingyue/fde-skills)

**人人都是 FDE 工程师。**

Awesome FDE 由 FDE中国社区发起。我们关心的不是“能否做出 Demo”，而是 AI 系统能否进入真实流程，安全、稳定、可度量地创造业务价值，并把一次性交付沉淀为可复用能力。

> 当前状态：`v0.1` 初始化版本。欢迎通过 Issue、Discussion 和 Pull Request 共建。

## 目录

* [项目定位](#项目定位)
* [什么是 FDE](#什么是-fde)
* [FDE 能力模型](#fde-能力模型)
* [四条学习路线](#四条学习路线)
* [学习资源](#学习资源)
* [企业 AI 项目交付体系](#企业-ai-项目交付体系)
* [本地研究报告](#本地研究报告)
* [仓库结构](#仓库结构)
* [收录标准](#收录标准)
* [参与贡献](#参与贡献)
* [社区路线图](#社区路线图)
* [免责声明与许可](#免责声明与许可)

## 项目定位

Awesome FDE 是“导航与索引层”，帮助读者快速找到可信资源、学习路线、工具图谱和交付模板。它与 FDE中国生态中的另外两个项目分工如下：

| 项目 | 定位 | 适合解决的问题 |
| --------------------------------------------------- | --------- | ----------------- |
| **Awesome FDE** | 精选资源与知识地图 | 应该学什么、用什么、交付什么 |
| [FDE Guide](https://github.com/bingyue/fde-guide) | 系统化中文教程 | 如何从客户发现走到生产交付 |
| [FDE Skills](https://github.com/bingyue/fde-skills) | 可执行能力包与模板 | 如何复用访谈、评估、上线与运营方法 |
| [FDEChina.ai](https://fdechina.ai/) | 社区与品牌入口 | 获取行业内容、实践交流与社区服务 |

本仓库不追求链接数量，而追求每条资源都能回答至少一个真实交付问题，并说明适用人群、使用边界和核验时间。

## 什么是 FDE

FDE 是一种客户近端、结果导向的工程角色或团队能力：深入客户或业务现场，把通用技术转化为特定业务结果，并把交付中发现的共性问题反馈给产品与平台。

它通常覆盖以下闭环：

```text
观察真实工作 → 定义问题与基线 → 设计与构建 → 评估与生产部署
      ↑                                              ↓
产品与平台反馈 ← 提炼可复用模式 ← 采纳与价值验证
```

判断一个岗位是否具有核心 FDE 属性，不看职位名称或驻场天数，而看四项责任是否同时成立：

| 判定维度 | 核心 FDE 的可观察证据 |
| ---- | ------------------------ |
| 结果责任 | 对上线、采用和业务结果负责，而非只交付方案或演示 |
| 工程深度 | 直接编写、测试、部署和维护可运行系统 |
| 客户共创 | 与业务、技术和一线用户持续迭代并形成联合决策 |
| 产品反馈 | 把重复问题沉淀为组件、模板、评估集或产品能力 |

FDE 与售前、实施顾问、系统集成、客户成功和产品工程均有交集，但关键差异是：**跨越问题发现、生产工程、结果验证和产品反馈，对端到端闭环负责。**

## FDE 能力模型

### 六域能力

| 能力域 | 核心问题 | 可观察产物 |
| ------- | -------------- | ---------------------- |
| 业务发现 | 哪个问题值得解决，谁承担结果 | 流程图、业务基线、机会卡、价值假设 |
| 软件与数据工程 | 能否把原型做成可运行系统 | 代码、测试、数据管道、接口、部署记录 |
| AI 系统工程 | 模型在真实任务分布上是否可靠 | 评估集、RAG/Agent 设计、回退与监控 |
| 客户共创 | 能否在模糊环境中形成联合决策 | 访谈、演示、迭代记录、采用计划 |
| 生产运营与治理 | 系统能否安全、持续运行 | 权限、审计、可观测、事故响应、SLO |
| 产品化与经营 | 项目经验能否复用并形成回报 | 复用资产、交付周期、单位结果成本、扩展 |

企业 AI 项目只具备单一 T 型能力往往不够。个人至少要有生产工程主干，并在业务流程、AI 可靠性、治理或产品化方向形成多根“梳齿”；个人不必覆盖全部，但小队必须覆盖。

### L1–L5 成长阶梯

| 级别 | 典型责任范围 | 关键跃迁 |
| -------------------- | ------------- | ---------- |
| L1 项目工程师 | 在明确问题内完成模块 | 从任务完成到理解用户 |
| L2 独立 FDE | 拥有一个工作流的端到端交付 | 从实现到上线和采用 |
| L3 FDE Lead | 领导多角色小队与客户决策 | 从单项目到项目组合 |
| L4 Principal FDE | 跨客户提炼产品模式 | 从交付到平台化 |
| L5 Deployment Leader | 设计组织、经营与生态网络 | 从团队到业务系统 |

完整说明见 [FDE 能力模型](./career/competency-model.md)。

## 四条学习路线

每条路线都以可检查产物为终点，而不是以“看完课程”为终点。

| 路线 | 适合人群 | 核心产物 | 入口 |
| ------------- | ------------------- | --------------------------- | --------------------------------------------- |
| AI 应用入门 | 产品、业务、传统软件工程师、转型者 | 一个有真实用户、结构化输出和基础评估的小应用 | [开始学习](./learning-paths/ai-beginner.md) |
| Agent 工程师 | 应用开发、全栈、自动化工程师 | 有状态、可追踪、可回退的 Agent/Workflow | [开始学习](./learning-paths/agent-engineer.md) |
| 企业 AI FDE | 解决方案、实施、咨询、AI 项目负责人 | 从机会卡到上线门禁与价值复盘的完整方案包 | [开始学习](./learning-paths/fde-engineer.md) |
| AI Infra 与生产化 | 平台、架构、SRE、MLOps 工程师 | 多模型服务、网关、评估、可观测与治理基线 | [开始学习](./learning-paths/ai-infra-engineer.md) |

不知道从哪里开始？先对照 [能力模型](./career/competency-model.md)，再选择与你当前职责最接近的一条路线。

## 学习资源

首版优先收录官方文档、公开课程、论文、技术报告和可复现工程资料。每个主题页都说明资源用途与适合人群。

| 主题          | 你需要解决的问题                            | 入口                                                          |
| ----------- | ----------------------------------- | ----------------------------------------------------------- |
| 大模型基础       | Transformer、Token、Embedding、推理与模型边界 | [LLM Foundations](./resources/llm-foundations.md)           |
| Prompt 与上下文 | 指令、结构化输出、上下文组织与可靠性                  | [Prompt & Context](./resources/prompt-and-context.md)       |
| AI Agent    | 状态、工具、记忆、规划、人机协同与多智能体               | [Agents](./resources/agents.md)                             |
| RAG 与知识库    | 解析、切分、检索、重排、权限与引用                   | [RAG & Knowledge](./resources/rag-and-knowledge.md)         |
| 模型部署        | 推理服务、吞吐、延迟、量化与硬件适配                  | [Model Deployment](./resources/model-deployment.md)         |
| 评测与 LLMOps  | 数据集、Trace、回归、漂移、成本与告警               | [LLMOps & Evaluation](./resources/llmops-and-evaluation.md) |
| AI 安全       | Prompt Injection、最小权限、审计、红队与供应链     | [AI Security](./resources/ai-security.md)                   |
| 综合课程        | 可按章节完成的系统课程                         | [Courses](./resources/courses.md)                           |
| 书籍          | 基础理论、系统设计与组织方法                      | [Books](./resources/books.md)                               |
| 论文          | 关键方法与评估研究                           | [Papers](./resources/papers.md)                             |
| 报告          | FDE、企业 AI 与生产部署观察                   | [Reports](./resources/reports.md)                           |

工具选型不是资源清单的终点。请从生产约束出发查看 [开源工具图谱](./tools/README.md)，重点评估许可证、维护状态、部署复杂度、安全边界和总拥有成本。

## 企业 AI 项目交付体系

交付主线来自两份本地 FDE 报告和现有 FDE Guide/Skills 实践，按“阶段、门禁、责任、证据”组织：

```text
机会发现 → 价值与可行性诊断 → PoC 降低不确定性 → 生产化
   → 采用与流程重构 → ROI 验证 → 产品化 / 长期运营 / 停止
```

| 阶段  | 核心决策               | 最小交付物                | 方法入口                                             |
| --- | ------------------ | -------------------- | ------------------------------------------------ |
| 发现  | 问题是否值得继续           | 访谈记录、现状流程、机会卡、业务基线   | [Discovery](./delivery/discovery.md)             |
| 方案  | 如何形成可控的最小闭环        | 架构决策、数据流、权限与风险设计     | [Solution Design](./delivery/solution-design.md) |
| PoC | 哪个关键不确定性被验证        | PoC 章程、真实任务集、阈值、退出结论 | [PoC](./delivery/poc.md)                         |
| 实施  | 系统能否被可靠构建与集成       | 代码、版本、测试、数据与接口记录     | [Implementation](./delivery/implementation.md)   |
| 评估  | 工作是否被正确完成          | 五层评估、回归集、错误分类、成本基线   | [Evaluation](./delivery/evaluation.md)           |
| 上线  | 是否通过价值、质量、风险、运营四道门 | 批准记录、回退演练、SLO、培训与交接  | [Go Live](./delivery/go-live.md)                 |
| 运营  | 是否扩大、保持、降级、产品化或停止  | 月度复盘、价值证明、事故与变更记录    | [Operations](./delivery/operations.md)           |

可直接复制的 [交付模板库](./templates/README.md) 已包含：

* 业务访谈提纲与机会卡
* 架构决策、RACI 与生产系统卡
* PoC 章程
* 项目计划与变更记录
* 供应商尽调、上线门禁、验收与审计证据索引
* 月度运营复盘、项目复盘与产品化检查

## 本地研究报告

仓库内的两份报告为本次初始化的主要方法论来源：

* [《2027中国FDE人才与企业AI落地实践报告》](./reports/2027中国FDE人才与企业AI落地实践报告对外传播版本.pdf) — FDE中国社区，覆盖岗位边界、六域能力、全生命周期、组织成长、路线图与审计证据包。
* [《FDE模式行业观察与实践》](./reports/FDE模式行业观察与实践.pdf) — 腾讯研究院，覆盖 FDE 前线学习机制、组织模式、人才考核、复用与规模化实践。

报告索引、引用边界与版权说明见 [reports/README.md](./reports/README.md)。

## 仓库结构

```text
awesome-fde/
├── README.md                     # 首页与总导航
├── CONTRIBUTING.md               # 贡献流程
├── CODE_OF_CONDUCT.md            # 社区行为准则
├── LICENSE                       # 原创内容与代码许可
├── NOTICE                        # 第三方材料与商标说明
├── SECURITY.md                   # 敏感信息与安全报告方式
├── .github/                      # Issue / PR 模板
├── reports/                      # 本地研究报告及引用说明
├── learning-paths/               # 四条分角色学习路线
│   ├── ai-beginner.md
│   ├── agent-engineer.md
│   ├── fde-engineer.md
│   └── ai-infra-engineer.md
├── resources/                    # 分类学习资源
│   ├── llm-foundations.md
│   ├── prompt-and-context.md
│   ├── agents.md
│   ├── rag-and-knowledge.md
│   ├── model-deployment.md
│   ├── llmops-and-evaluation.md
│   ├── ai-security.md
│   ├── courses.md
│   ├── books.md
│   ├── papers.md
│   └── reports.md
├── tools/                        # 开源工具与产品图谱
│   ├── application-platforms.md
│   ├── agent-frameworks.md
│   ├── vector-databases.md
│   ├── model-serving.md
│   ├── ai-gateways.md
│   └── observability.md
├── delivery/                     # 企业 AI 全生命周期方法
│   ├── discovery.md
│   ├── solution-design.md
│   ├── poc.md
│   ├── implementation.md
│   ├── evaluation.md
│   ├── go-live.md
│   └── operations.md
├── templates/                    # 可直接复制的交付模板
│   ├── discovery/
│   ├── solution/
│   ├── poc/
│   ├── implementation/
│   ├── acceptance/
│   └── retrospective/
├── cases/                        # 经授权与脱敏的行业案例
│   ├── manufacturing/
│   ├── ecommerce/
│   ├── retail/
│   ├── finance/
│   ├── customer-service/
│   ├── hr-and-admin/
│   └── global-growth/
├── career/                       # 能力、作品集、面试与岗位地图
└── community/                    # 路线图、活动与贡献者
```

## 收录标准

### 优先收录

* 官方文档、公开课程、论文、技术报告与活跃开源项目
* 有清晰作者、来源、许可证和核验日期的资料
* 能解决企业 AI 场景、工程生产化或项目交付问题的内容
* 提供示例、代码、评估方法、失败边界或可复用模板的资料
* 已获得授权并完成脱敏的真实案例

### 谨慎或不收录

* 只有营销描述、无法验证关键能力的内容
* 长期无人维护、文档缺失或许可证不清晰的项目
* 聚合转载、来源不明、标题夸张或重复度高的文章
* 包含客户敏感数据、个人信息、密钥或不当数据处理方式的材料
* 将供应商自述、预计收益或试点指标写成独立验证结论的案例

每条新增资源使用统一格式：

```markdown
- [资源名称](链接) — 适合谁、解决什么问题。`中文/英文` `免费/付费` `核验：YYYY-MM-DD`
```

完整审查维度见 [贡献指南](./CONTRIBUTING.md)。

## 参与贡献

欢迎贡献资源、工具、学习路线、交付模板、脱敏案例、失效链接和事实勘误。

1. Fork 仓库并创建单一主题分支。
2. 使用现有页面格式添加内容，补齐来源、适用场景、限制和核验日期。
3. 检查站内相对链接、外部链接、版权、许可证和脱敏情况。
4. 提交 Pull Request，说明新增价值、证据来源及潜在利益关系。

开始前请阅读 [CONTRIBUTING.md](./CONTRIBUTING.md) 与 [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)。安全漏洞、密钥或未脱敏数据请勿提交公开 Issue，处理方式见 [SECURITY.md](./SECURITY.md)。

## 社区路线图

* [x] 建立项目定位、能力模型和四条学习路线
* [x] 建立 LLM、Agent、RAG、AI Infra、评测与安全资源骨架
* [x] 建立企业 AI 全生命周期与首批交付模板
* [ ] 完成首批 100 条资源的维护状态与许可证复核
* [ ] 发布 10 个经过授权和脱敏的完整案例
* [ ] 建立季度失效链接与内容更新机制
* [ ] 建立中文 FDE 岗位、作品集和面试资料库
* [ ] 将优秀项目沉淀为可复用 Skill、连接器和评估资产

详细里程碑与验收标准见 [community/roadmap.md](./community/roadmap.md)。

## 免责声明与许可

* 本仓库用于学习、研究与行业交流，不构成技术、法律、合规、投资或采购建议。
* 收录外部链接不代表 FDE中国社区对相关内容、产品或服务背书。
* 产品能力、模型价格、项目状态、法规和标准可能变化，生产使用前请以最新官方信息与专业意见为准。
* 企业案例必须获得授权并去除客户名称、个人信息、商业秘密与生产凭据。
* 供应商自述、预计 ROI、目标值和样本结果必须保留来源、时间、口径和限制。
* 仓库原创 Markdown 与代码按 [MIT License](./LICENSE) 提供；第三方报告、商标和外部内容不因此改变权利归属，详见 [NOTICE](./NOTICE)。

## FDEChina.ai

[FDEChina.ai](https://fdechina.ai/) 是 FDE中国社区的品牌与服务入口，连接企业真实需求、工程交付能力、行业实践和人才成长。

如果这个项目对你有帮助，欢迎 Star、分享、提交 Issue 或 Pull Request，一起把“会用 AI”推进到“能在企业里交付 AI”。
