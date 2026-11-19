# 数据集与评测样本

企业数据集应从授权与业务任务开始，而非先选择公开排行榜。

| 来源 | 用途 | 限制 |
| --- | --- | --- |
| [本仓库合成样本](../cookbook/examples/fixtures.json) | 学习过滤、引用、弃答与幂等 | 不能代表真实业务分布 |
| [Golden Dataset模板](../toolkit/templates/golden-dataset.md) | 登记来源、标注、分层与版本 | 需业务专家复核 |
| [Hugging Face Datasets](https://huggingface.co/docs/datasets/) | 加载与处理已获许可的数据集 | 每个数据集单独检查许可、用途和个人信息 |

原始样本、开发集、盲测集与线上回归集应可追溯。公开数据不自动意味着允许任意再分发。
