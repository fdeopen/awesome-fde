# 企业 AI 交付模板库

模板用于让业务、工程、数据、治理和财务在同一份事实底稿上决策。它们不是认证标准，也不能替代法务、信息安全、内审或监管判断。

| 阶段 | 模板 | 用途 |
| --- | --- | --- |
| 发现 | [业务访谈提纲](./discovery/interview-guide.md) | 访谈战略、运营与一线角色 |
| 发现 | [机会卡](./discovery/opportunity-card.md) | 把模糊愿望变成可验证命题 |
| 方案 | [架构决策记录](./solution/architecture-decision-record.md) | 保存选型、约束和权衡 |
| 方案 | [RACI 责任矩阵](./solution/raci.md) | 明确业务、技术、数据、治理和运营责任 |
| 方案 | [生产 AI 系统卡](./solution/system-card.md) | 登记实际模型、数据、工具、权限与运行配置 |
| PoC | [PoC 章程](./poc/poc-charter.md) | 验证关键假设并设置退出条件 |
| 实施 | [项目计划](./implementation/project-plan.md) | 管理里程碑、责任、依赖与变更 |
| 验收 | [供应商尽调](./acceptance/vendor-due-diligence.md) | 核对数据、权限、变更、安全与退出责任 |
| 验收 | [上线门禁](./acceptance/launch-gate.md) | 完成价值、质量、风险与运营评审 |
| 验收 | [验收报告](./acceptance/acceptance-report.md) | 汇总证据、剩余风险和结论 |
| 验收 | [审计证据索引](./acceptance/audit-evidence-index.md) | 让关键决策、权限、版本和结果可重建 |
| 运营 | [月度运营复盘](./retrospective/monthly-operations-review.md) | 决定扩大、保持、缩小、降级或停止 |
| 复盘 | [项目复盘](./retrospective/project-retrospective.md) | 记录价值、失败、资产和下一步 |

## 使用原则

1. 复制模板到具体项目目录后填写，不直接在模板上写客户信息。
2. 使用稳定 ID 关联需求、版本、评估、变更、事故和业务结果。
3. 任何敏感字段只保存引用位置，不把生产密钥或完整个人信息写入文档。
4. 每个门禁都记录批准人、日期、证据和不通过时动作。
