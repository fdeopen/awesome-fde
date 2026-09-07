# AI Gateway

AI Gateway 用于统一模型访问、认证、路由、配额、审计、成本和降级。它不能替代应用侧的业务权限与工具授权。

| 项目 | 核心能力 | 评估重点 | 官方入口 |
| --- | --- | --- | --- |
| LiteLLM | 多模型统一 API、路由、预算和代理 | 模型兼容、密钥托管、故障转移和成本口径 | [GitHub](https://github.com/BerriAI/litellm) · [文档](https://docs.litellm.ai/docs/) |
| Envoy AI Gateway | 基于 Envoy Gateway 的 AI 流量治理 | Kubernetes 集成、策略、扩展性和成熟度 | [GitHub](https://github.com/envoyproxy/ai-gateway) · [文档](https://aigateway.envoyproxy.io/) |
| Kong AI Gateway | API Gateway 上的 AI 路由与治理 | 插件、鉴权、可观测、部署形态和商业边界 | [文档](https://developer.konghq.com/ai-gateway/) |
| Portkey AI Gateway | 多模型网关、Guardrail 与可观测 | 托管/自部署边界、数据处理和供应商锁定 | [GitHub](https://github.com/Portkey-AI/gateway) · [文档](https://portkey.ai/docs/) |

`核验：2026-09-07`。

## 最小策略

- 用户、应用、租户和环境分层认证
- 模型白名单、版本策略、超时、重试和熔断
- Token 与金额预算、并发和速率限制
- 敏感数据处理、区域路由和日志最小化
- 请求、模型版本、Trace、成本与业务结果的稳定 ID 关联
- 主模型不可用时的替代模型或非 AI 业务降级
