# 升级前资产盘点

盘点日期：2026-11-19；基线提交：`142ed13725b12289269805b6bc16114f9abf16af`。目标仓库为既有 Awesome-FDE，公开地址已转至 FDEOpen，旧 SSH origin 仍可访问同一提交。

| 资产 | 数量 | 处理 |
| --- | ---: | --- |
| Git 跟踪文件 | 76 | 全部保留路径 |
| Markdown | 66 | 首页重构，其余通过新索引复用 |
| 角色学习路线 | 4 | 与新增三级路线并存 |
| 生命周期方法 | 7 | 关联新增 12 阶段 Playbook |
| 可复制模板 | 13 | 原路径保留，新增工具箱补齐场景 |
| 行业说明页 | 7 | 保留边界说明，增加实际阅读索引 |
| PDF 报告 | 2 | 原文件保留，不改授权 |
| GitHub Actions | 0 | 增加文档门禁和定期维护 |
| 图书与代码示例 | 0 | 新建配套导航和离线教学示例 |

## 关联资产与重构决定

- FDE中国网站本地快照含 119 篇外部案例文章、5 篇教学/PoC 材料、151 篇知识文章；三类数量分别统计，不合并宣称 200 个真实项目。
- `fdeopen/fde-case-study` 公开页面当前为空仓库；仅列为后续协作入口，不声称有已发布案例。
- 现有 FDE Guide、FDE Skills、能力模型、工具页与报告均保留；新增模块负责索引、练习和增量内容。
- 本地 FDE中国图书配置提供正式封面与目录；12 个章名已逐一匹配出版社正式目录。目录小节仅用于导航，正文不迁入。
- 原创资料继续适用 MIT。封面、目录、第三方材料不因收录改变权属。

## 基线文件清单

- `.gitattributes`
- `.github/ISSUE_TEMPLATE/case.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/resource.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.gitignore`
- `.markdownlint.json`
- `CODE_OF_CONDUCT.md`
- `CONTRIBUTING.md`
- `LICENSE`
- `NOTICE`
- `README.md`
- `SECURITY.md`
- `career/README.md`
- `career/competency-model.md`
- `career/interview-guide.md`
- `career/job-map.md`
- `career/portfolio-guide.md`
- `cases/README.md`
- `cases/customer-service/README.md`
- `cases/ecommerce/README.md`
- `cases/finance/README.md`
- `cases/global-growth/README.md`
- `cases/hr-and-admin/README.md`
- `cases/manufacturing/README.md`
- `cases/retail/README.md`
- `community/contributors.md`
- `community/events.md`
- `community/roadmap.md`
- `delivery/discovery.md`
- `delivery/evaluation.md`
- `delivery/go-live.md`
- `delivery/implementation.md`
- `delivery/operations.md`
- `delivery/poc.md`
- `delivery/solution-design.md`
- `learning-paths/agent-engineer.md`
- `learning-paths/ai-beginner.md`
- `learning-paths/ai-infra-engineer.md`
- `learning-paths/fde-engineer.md`
- `reports/2027中国FDE人才与企业AI落地实践报告对外传播版本.pdf`
- `reports/FDE模式行业观察与实践.pdf`
- `reports/README.md`
- `resources/README.md`
- `resources/agents.md`
- `resources/ai-security.md`
- `resources/books.md`
- `resources/courses.md`
- `resources/llm-foundations.md`
- `resources/llmops-and-evaluation.md`
- `resources/model-deployment.md`
- `resources/papers.md`
- `resources/prompt-and-context.md`
- `resources/rag-and-knowledge.md`
- `resources/reports.md`
- `templates/README.md`
- `templates/acceptance/acceptance-report.md`
- `templates/acceptance/audit-evidence-index.md`
- `templates/acceptance/launch-gate.md`
- `templates/acceptance/vendor-due-diligence.md`
- `templates/discovery/interview-guide.md`
- `templates/discovery/opportunity-card.md`
- `templates/implementation/project-plan.md`
- `templates/poc/poc-charter.md`
- `templates/retrospective/monthly-operations-review.md`
- `templates/retrospective/project-retrospective.md`
- `templates/solution/architecture-decision-record.md`
- `templates/solution/raci.md`
- `templates/solution/system-card.md`
- `tools/README.md`
- `tools/agent-frameworks.md`
- `tools/ai-gateways.md`
- `tools/application-platforms.md`
- `tools/model-serving.md`
- `tools/observability.md`
- `tools/vector-databases.md`
