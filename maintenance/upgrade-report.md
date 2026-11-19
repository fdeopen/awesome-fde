# Awesome-FDE升级交付报告

日期：2026-11-19。基线提交：`142ed13725b12289269805b6bc16114f9abf16af`。本报告记录升级的本地验收结果；后续按作者指令提交至原Awesome-FDE仓库，未创建替代主仓库。

## 定位变化

升级前：面向FDE与企业AI实践者的中文精选资源库。

升级后：Awesome-FDE · 企业AI交付开放指南，兼具作者图书配套入口和长期开放实践平台，连接FDE中国、FDEOpen与51FDE。保持MIT许可、原仓库历史及既有文件路径。公开地址为FDEOpen组织下原项目；按作者指令将本地origin统一为 `git@github.com:fdeopen/awesome-fde.git`，保留原提交历史。

## 交付数量与范围

| 内容 | 数量 | 完成边界 |
| --- | ---: | --- |
| 核心模块 | 8 | 均有导航与实际内容 |
| 中英文首页 | 2 | 图书、学习、交付、社区、贡献和许可 |
| 图书学习章页 | 12 | 每章有目标、知识地图、资料、框架、案例、模板、任务、FAQ与更新 |
| 正式目录小节 | 154 | 12章章名、小节、编号和页码；未复制正文 |
| 新三级路线 | 3 | 阶段目标、资料、项目与能力验收 |
| 原角色路线 | 4 | 原路径保留 |
| 交付阶段 | 12 | 目标、输入输出、方法、风险、模板与案例 |
| 工具箱核心模板 | 30 | 25份新增，5份复用并增补示例 |
| 全部交付模板 | 38 | 原13份 + 新25份，不重复计算索引页 |
| 工程配方 | 10 | LLM、RAG、Agent、多智能体、Skill、MCP、Harness、本体、评测、部署 |
| 可运行教学程序 | 2 | 离线控制练习、ROI计算器；不依赖外部模型 |
| 社区文章索引 | 119 | 标题、摘要、原行业、分类、日期、链接与证据边界 |
| 完整模拟案例 | 1 | 14项统一结构，全部使用合成数据 |
| 项目简报 | 10 | 2项关联同一离线示例、1项公开本体知识仓库，其余7项规划；不是10套成品应用 |
| 重点技术项目 | 20 | 官方仓库/文档、场景、特征、许可、限制、核验日 |
| 技术架构分类 | 20 | 含国内外生态和大陆部署注意事项 |
| Issue类型 | 7 | 勘误、资源、案例、项目、模板、工程问题、社区建议 |
| GitHub工作流 | 2 | PR离线门禁；每周外链与贡献者维护草稿 |

## 目录结构

```text
awesome-fde/
├── README.md / README_EN.md
├── CONTRIBUTING.md / CODE_OF_CONDUCT.md / SECURITY.md
├── ROADMAP.md / CHANGELOG.md / LICENSE / NOTICE
├── assets/                     # 正式封面、品牌说明
├── book/                       # 元数据、正式目录、12章配套、勘误与FAQ
├── roadmap/                    # 三条成长路线、能力与职业导航
├── playbook/                   # 12阶段方法
├── toolkit/                    # 25份新增模板、检查单、评测、提示词、ROI工具
├── cookbook/                   # 10份配方与离线合成练习
├── cases/                      # 119篇索引、旧行业入口、完整模拟案例
├── projects/                   # 10项项目简报、状态与贡献模板
├── resources/                  # 旧学习资源、20项技术图谱及数据/社区导航
├── community/                  # 生态、贡献者、活动、初次贡献任务
├── learning-paths/             # 保留4条角色路线
├── career/                     # 保留能力模型、作品集、面试与岗位
├── delivery/                   # 保留7阶段详细方法
├── templates/                  # 保留13份原模板
├── tools/                      # 保留6类旧工具图谱
├── reports/                    # 保留2份PDF及版权说明
├── maintenance/                # 盘点、迁移、核验与本报告
├── scripts/                    # 元数据生成、内外链检查、贡献者草稿
└── .github/                    # 7种Issue表单、PR模板、2个工作流
```

## 历史资产与兼容

76个既有跟踪文件全部保留，无删除或移动。原13份模板、4条角色路线、7阶段方法、职业内容、资源图谱及2份PDF均可继续访问。首页旧目录锚点保留，旧入口转入新知识模块。原许可证原文不变，NOTICE补充图书、案例与模拟数据边界。

详细资产清单见[升级前盘点](asset-inventory.md)，维护方式见[兼容性说明](migration.md)。图书事实、正式章序、生态、案例与工具集中保存JSON，通过生成器同步Markdown，降低多处硬编码造成的漂移。

## 图书依据

- 正式封面沿用FDE中国本地项目保存的出版社原图，并完成视觉核对。
- 正式书名、作者、出版社、ISBN、出版日期及京东/天猫入口已与出版社页面核对。
- 12个章名及154个小节与出版社完整目录逐项对齐；空白、全角标点归一化后匹配。
- 销量2000+来自作者本次需求，明确标为作者提供，并非独立审计结论。
- 出版事实与来源见[metadata.json](../book/metadata.json)，配套内容见[图书中心](../book/README.md)。

## 验证结果

| 检查 | 结果 |
| --- | --- |
| Markdown格式 | 178篇通过markdownlint-cli 0.45.0检查 |
| 内部链接、锚点、图片和目录 | 配套资料入口统一后794条内部引用检查通过，0错误；封面已视觉核对 |
| 元数据生成与文档构建 | render.py --check通过，无生成内容漂移 |
| 离线控制示例 | 7项断言通过，包含越权、弃答、过期、幂等与冲突 |
| ROI模型 | 7项数值与边界检查通过；零净收益无回收期，零投入不计算ROI |
| YAML | 10份配置解析通过，其中7种Issue表单和2套工作流 |
| Python | 脚本语法编译通过，运行示例与计算器通过 |
| Git空白与历史路径 | diff --check通过；76个历史路径均存在，0删除 |
| 外部链接 | 当前279个URL：276可访问、0待修复、3访问受限 |
| 社区案例链接 | 119/119可访问；可访问不等于独立验证文章事实 |

3个受限链接均为O’Reilly图书页，返回HTTP403，已保留来源并记录在 `external-links.json`。首次全量检查发现Star列表页与旧Microsoft框架仓库返回404：前者徽章点击已改至可访问的仓库主页；后者保留历史名称与待核验说明，移除失效点击入口。最终外链快照在首次全量检查后，仅对新增或变化URL补查，避免重复请求。

工作流本地配置与相同检查命令已通过；云端运行结果以提交后的GitHub Actions记录为准。两份原PDF未修改，本次不重新验证其全文事实或再分发授权。

## 尚未完成与需作者提供的资源

1. 200份案例的完整来源目录尚未定位：目前只有119篇社区外部文章快照，全部作为索引收录。需要提供剩余来源清单及公开范围，不以知识文章或模拟条目补足数量。
2. fde-case-study公开仓库核验时为空；待发布内容后建立双向索引。
3. 10项应用方向尚未全部实现。本次交付的是可审核的项目简报、参考组件和离线练习；后续逐个补源码、部署包、模拟数据及实际运行报告。
4. 原有Microsoft Agent Framework仓库地址本次返回404，历史条目保留并标待核验，当前重点图谱使用已确认存在的项目。
5. 封面与购书链接已找到，无需再次提供。建议作者确认配套练习与章内意图一致，并指定销量更新与勘误维护责任人。
6. GitHub Actions配置已本地验证，云端首次运行需提交后触发。本次没有新建Issue或部署独立应用。

## 后续30天运营建议

- 第1周：作者复核12章任务与勘误流程，公布统一项目入口；各生态站点指向同一仓库。
- 第2周：选5篇案例追溯一手来源，修正分类，明确效果数据的披露条件；继续定位200份来源。
- 第3周：邀请两位实践者试填模板并复现练习，收集可公开反馈，合并小范围PR。
- 第4周：优先完成知识助手或RAG评测的独立应用，发布模拟数据、干净环境运行步骤和评测证据。

长期按[ROADMAP](../ROADMAP.md)执行季度链接与许可证复核；社区维护草稿经审核后再合并，不自动向主分支写入。

## 修改文件清单

27个既有文件修改：

- `.github/ISSUE_TEMPLATE/case.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.gitignore`
- `.markdownlint.json`
- `CONTRIBUTING.md`
- `NOTICE`
- `README.md`
- `SECURITY.md`
- `cases/README.md`
- `cases/customer-service/README.md`
- `cases/ecommerce/README.md`
- `cases/finance/README.md`
- `cases/global-growth/README.md`
- `cases/hr-and-admin/README.md`
- `cases/manufacturing/README.md`
- `cases/retail/README.md`
- `community/contributors.md`
- `community/roadmap.md`
- `resources/README.md`
- `resources/agents.md`
- `resources/books.md`
- `templates/acceptance/launch-gate.md`
- `templates/discovery/interview-guide.md`
- `templates/implementation/project-plan.md`
- `templates/poc/poc-charter.md`
- `templates/retrospective/project-retrospective.md`
- `tools/agent-frameworks.md`

## 新增文件清单

133个新增文件（含本报告）：

- `.github/ISSUE_TEMPLATE/book-errata.yml`
- `.github/ISSUE_TEMPLATE/community.yml`
- `.github/ISSUE_TEMPLATE/engineering.yml`
- `.github/ISSUE_TEMPLATE/project.yml`
- `.github/ISSUE_TEMPLATE/template.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/maintenance.yml`
- `CHANGELOG.md`
- `README_EN.md`
- `ROADMAP.md`
- `assets/brand/README.md`
- `assets/images/fde-frontline-cover.jpg`
- `book/README.md`
- `book/author.md`
- `book/chapters.json`
- `book/chapters/01.md`
- `book/chapters/02.md`
- `book/chapters/03.md`
- `book/chapters/04.md`
- `book/chapters/05.md`
- `book/chapters/06.md`
- `book/chapters/07.md`
- `book/chapters/08.md`
- `book/chapters/09.md`
- `book/chapters/10.md`
- `book/chapters/11.md`
- `book/chapters/12.md`
- `book/errata.md`
- `book/faq.md`
- `book/introduction.md`
- `book/metadata.json`
- `book/table-of-contents.md`
- `cases/case-template.md`
- `cases/catalog.json`
- `cases/catalog.md`
- `cases/enterprise-services/README.md`
- `cases/enterprise-services/synthetic-service-desk.md`
- `community/README.md`
- `community/ecosystem.json`
- `community/good-first-issues.md`
- `cookbook/README.md`
- `cookbook/agent/README.md`
- `cookbook/deployment/README.md`
- `cookbook/evaluation/README.md`
- `cookbook/examples/README.md`
- `cookbook/examples/fixtures.json`
- `cookbook/examples/offline_delivery.py`
- `cookbook/harness/README.md`
- `cookbook/llm/README.md`
- `cookbook/mcp/README.md`
- `cookbook/multi-agent/README.md`
- `cookbook/ontology/README.md`
- `cookbook/rag/README.md`
- `cookbook/skill/README.md`
- `learning-paths/README.md`
- `maintenance/README.md`
- `maintenance/asset-inventory.md`
- `maintenance/external-links.json`
- `maintenance/migration.md`
- `maintenance/upgrade-report.md`
- `playbook/README.md`
- `playbook/business-discovery/README.md`
- `playbook/business-value/README.md`
- `playbook/data-governance/README.md`
- `playbook/evaluation/README.md`
- `playbook/implementation/README.md`
- `playbook/ontology-modeling/README.md`
- `playbook/poc-delivery/README.md`
- `playbook/production-delivery/README.md`
- `playbook/productization/README.md`
- `playbook/requirements/README.md`
- `playbook/scenario-design/README.md`
- `playbook/solution-design/README.md`
- `projects/README.md`
- `projects/commerce-analytics.md`
- `projects/enterprise-ontology.md`
- `projects/knowledge-assistant.md`
- `projects/knowledge-cleaning.md`
- `projects/manufacturing-quote.md`
- `projects/process-document.md`
- `projects/production-agent.md`
- `projects/project-catalog.md`
- `projects/project-template.md`
- `projects/rag-evaluation.md`
- `projects/sales-training.md`
- `projects/trade-prospecting.md`
- `resources/catalog.json`
- `resources/communities.md`
- `resources/datasets.md`
- `resources/frameworks.md`
- `resources/open-source.md`
- `resources/tools.md`
- `roadmap/README.md`
- `roadmap/advanced.md`
- `roadmap/beginner.md`
- `roadmap/career-guide.md`
- `roadmap/competency-model.md`
- `roadmap/intermediate.md`
- `scripts/check_docs.py`
- `scripts/check_external.py`
- `scripts/render.py`
- `scripts/update_contributors.py`
- `toolkit/README.md`
- `toolkit/calculators/README.md`
- `toolkit/calculators/roi.py`
- `toolkit/checklists/README.md`
- `toolkit/evaluation/README.md`
- `toolkit/prompts/README.md`
- `toolkit/templates/agent-design.md`
- `toolkit/templates/agent-evaluation.md`
- `toolkit/templates/bad-case.md`
- `toolkit/templates/data-governance.md`
- `toolkit/templates/golden-dataset.md`
- `toolkit/templates/handover.md`
- `toolkit/templates/maturity.md`
- `toolkit/templates/mcp-interface.md`
- `toolkit/templates/ontology.md`
- `toolkit/templates/poc-acceptance.md`
- `toolkit/templates/priority.md`
- `toolkit/templates/process-map.md`
- `toolkit/templates/quotation.md`
- `toolkit/templates/rag-design.md`
- `toolkit/templates/rag-evaluation.md`
- `toolkit/templates/requirements.md`
- `toolkit/templates/risk-register.md`
- `toolkit/templates/roi.md`
- `toolkit/templates/scenario-discovery.md`
- `toolkit/templates/scenario-score.md`
- `toolkit/templates/security-governance.md`
- `toolkit/templates/skill-design.md`
- `toolkit/templates/solution.md`
- `toolkit/templates/system-data.md`
- `toolkit/templates/technology-selection.md`
