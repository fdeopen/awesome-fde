# 离线交付练习

只需Python 3标准库，无API密钥、模型下载或外部服务。

```bash
python3 cookbook/examples/offline_delivery.py
```

预期输出 `passed: 7`：4条检索/弃答断言，加幂等重试、越权拒绝与幂等冲突3条断言。样本均在[fixtures.json](fixtures.json)中明确标为合成。

## 能学到什么

- 检索之前过滤租户和失效文档。
- 引用文档ID，无证据时弃答。
- 写入沙箱草稿前验证身份，以租户和请求ID保证单进程幂等。
- 同一幂等键但不同输入必须拒绝，不能悄悄覆盖。

## 边界

代码不调用大模型、不实现MCP服务器，也没有真实鉴权或持久化。生产系统必须替换身份来源、事务存储、审计和故障恢复；不能把字符串相等检查直接作为登录授权。这里的“草稿”只写入进程内列表，不触达任何业务系统。

修改代码后，用[模拟案例](../../cases/enterprise-services/synthetic-service-desk.md)说明业务含义，再填写[评测报告](../../toolkit/templates/agent-evaluation.md)。
