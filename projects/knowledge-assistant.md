# 企业级知识库问答助手

状态：已有离线控制示例；完整应用规划中。难度：入门。关联[图书章节](../book/table-of-contents.md)：第8、10章。

## 场景与项目范围

售后政策与内部制度查询。第一版只验证最关键的一条业务链路，业务动作保留人工确认。

## 技术架构与选型

RAGFlow或现有搜索 + ACL +引用。对照[技术图谱](../resources/frameworks.md)与[选型矩阵](../toolkit/templates/technology-selection.md)，依据数据规模、权限和团队部署能力决定具体版本。

## 源代码与部署状态

[本仓库离线源代码](../cookbook/examples/offline_delivery.py)可用Python标准库运行，步骤见[README](../cookbook/examples/README.md)。完整应用尚未发布。

## 模拟数据设计

合成文档与租户问题。至少包括正常、缺字段、冲突、越权和无答案五组；真实企业数据替换前需重建授权、质量与评测基线。现有样例见[fixtures.json](../cookbook/examples/fixtures.json)。

## 评测与验收

跨租户召回0、无依据弃答。另外记录成本、延迟、失败与人工复核量。交付时提供版本、逐题结果和复现命令；应用完成后才能升级“可运行”状态。
