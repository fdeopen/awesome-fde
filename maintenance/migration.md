# 兼容性与维护

新增八大模块作为统一导航；历史文件不搬迁、不删除。旧的书签、外部引用和图书链接继续有效。

| 历史入口 | 新入口 | 维护规则 |
| --- | --- | --- |
| learning-paths/ | [roadmap](../roadmap/README.md) | 按角色与按成长阶段互补 |
| career/ | [能力模型](../roadmap/competency-model.md) | 能力定义仍在 career 维护 |
| delivery/ | [playbook](../playbook/README.md) | 原方法仍为详细参考 |
| templates/ | [toolkit](../toolkit/README.md) | 原 13 份不重复复制 |
| tools/ | [技术资源图谱](../resources/frameworks.md) | 旧条目保留历史核验日 |
| community/roadmap.md | [ROADMAP](../ROADMAP.md) | 保留历史里程碑并链接新计划 |

## 单一来源

图书事实维护在 `book/metadata.json`，章名/页码维护在 `book/chapters.json`；案例索引数据在 `cases/catalog.json`，技术图谱数据在 `resources/catalog.json`。编辑后运行 `python3 scripts/render.py`，提交源文件与生成的 Markdown。生成器 `--check` 验证是否同步。

首页图书块和生态块采用带标记的生成区域，保留人工撰写的其余内容。不要手工修改生成区域。

## 检查命令

```bash
python3 scripts/render.py --check
python3 scripts/check_docs.py
python3 cookbook/examples/offline_delivery.py
npx --yes markdownlint-cli@0.45.0 '**/*.md' '.github/**/*.md'
git diff --check
```

外链单独执行 `python3 scripts/check_external.py`；定时任务上传结果，不作为普通 PR 的合并门禁。Contributor 列表由 Git 历史生成，不披露邮箱。
