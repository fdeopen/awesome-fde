# 模型服务

| 项目 | 典型定位 | 生产评估重点 | 官方入口 |
| --- | --- | --- | --- |
| vLLM | 高吞吐 LLM 服务 | 连续批处理、KV Cache、兼容性、分布式与监控 | [GitHub](https://github.com/vllm-project/vllm) · [文档](https://docs.vllm.ai/) |
| SGLang | LLM/VLM 高性能服务与编程 | 前缀缓存、并行、模型支持和运行稳定性 | [GitHub](https://github.com/sgl-project/sglang) · [文档](https://docs.sglang.ai/) |
| Text Generation Inference | Hugging Face 推理服务 | 支持模型、量化、部署方式和维护状态 | [GitHub](https://github.com/huggingface/text-generation-inference) · [文档](https://huggingface.co/docs/text-generation-inference/) |
| llama.cpp | 轻量、本地和边缘推理 | 模型格式、硬件后端、上下文和性能边界 | [GitHub](https://github.com/ggml-org/llama.cpp) |
| Ollama | 本地模型运行与分发 | 开发体验好；生产需额外评估并发、治理和运维 | [GitHub](https://github.com/ollama/ollama) · [文档](https://docs.ollama.com/) |
| NVIDIA Triton | 多框架推理服务 | 动态批处理、模型仓库、指标、GPU 调度 | [GitHub](https://github.com/triton-inference-server/server) · [文档](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/) |

`核验：2026-09-07`。

性能结果必须绑定模型版本、量化、硬件、上下文长度、请求分布和并发；脱离这些条件的吞吐数字不可比较。
