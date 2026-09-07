# 模型部署与推理

目标：理解模型服务的吞吐、延迟、显存、并发、量化、缓存、路由和版本治理。

- [vLLM Documentation](https://docs.vllm.ai/) — 高吞吐大模型推理与 OpenAI 兼容服务。`英文` `免费` `核验：2026-09-07`
- [SGLang Documentation](https://docs.sglang.ai/) — 大模型与多模态模型的高性能服务框架。`英文` `免费` `核验：2026-09-07`
- [Hugging Face Text Generation Inference](https://huggingface.co/docs/text-generation-inference/) — Hugging Face 的生产级推理服务。`英文` `免费` `核验：2026-09-07`
- [llama.cpp](https://github.com/ggml-org/llama.cpp) — 支持多种硬件的轻量本地推理项目。`英文` `免费` `核验：2026-09-07`
- [Ollama Documentation](https://docs.ollama.com/) — 本地运行与管理开源模型。`英文` `免费` `核验：2026-09-07`
- [NVIDIA Triton Inference Server](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/) — 多框架模型服务、批处理与监控。`英文` `免费` `核验：2026-09-07`

## 压测至少报告

- 模型与量化版本、硬件、上下文长度和请求分布
- TTFT、每 Token 延迟、端到端延迟的 P50/P95/P99
- 吞吐、并发、显存、错误率和降级行为
- 每次请求、每个完成任务与每个合格结果的成本
