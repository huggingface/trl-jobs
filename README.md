# TRL Jobs

A convenient wrapper around `hfjobs` for running TRL (Transformer Reinforcement Learning) specific workflows on Hugging Face infrastructure.

## Installation

```bash
pip install trl-jobs
```

## Quick Start

```bash
trl-jobs sft --model_name Qwen/Qwen3-0.6B --dataset_name trl-lib/Capybara
```

## Available Commands

For now only SFT (Supervised Fine-Tuning) is supported.

### SFT (Supervised Fine-Tuning)

```bash
trl-jobs sft --flavor a100-large --model_name Qwen/Qwen3-0.6B --dataset_name trl-lib/Capybara
```

#### Required Arguments

- `--model_name`: Model name (e.g., `Qwen/Qwen3-0.6B`)
- `--dataset_name`: Dataset name (e.g., `trl-lib/Capybara`)

#### Optional Arguments

- `--flavor`: Hardware flavor (default: `a100-large`)
- `-d, --detach`: Run job in background and print job ID
- `--token`: Hugging Face access token

and any other arguments supported by `trl sft`. Please refer to the [TRL documentation](https://huggingface.co/docs/trl/en/clis)

### Supported Configurations

#### OpenAI GPT-OSS with PEFT

Coming soon!

#### Meta LLaMA 3

| Model | Maximum context length | # of tokens per effective batch size | Command |
| --- | --- | --- | --- |
| [meta-llama/Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B) | 4096 | 262144 | `trl-jobs sft --model_name meta-llama/Meta-Llama-3-8B --dataset_name ...` |
| [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) | 4096 | 262144 | `trl-jobs sft --model_name meta-llama/Meta-Llama-3-8B-Instruct --dataset_name ...` |

#### Meta LLaMA 3 with PEFT

| Model | Maximum context length | # of tokens per effective batch size | Command |
| --- | --- | --- | --- |
| [meta-llama/Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B) | 24576 | 196608 | `trl-jobs sft --model_name meta-llama/Meta-Llama-3-8B --peft --dataset_name ...` |
| [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) | 24576 | 196608 | `trl-jobs sft --model_name meta-llama/Meta-Llama-3-8B-Instruct --peft --dataset_name ...` |

#### Qwen3

| Model | Maximum context length | # of tokens per effective batch size | Command |
| --- | --- | --- | --- |
| [Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) | 32768 | 65536 | `trl-jobs sft --model_name Qwen/Qwen3-0.6B --dataset_name ...` |
| [Qwen/Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) | 24576 | 98304 | `trl-jobs sft --model_name Qwen/Qwen3-1.7B --dataset_name ...` |
| [Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) | 20480 | 163840 | `trl-jobs sft --model_name Qwen/Qwen3-1.7B --dataset_name ...` |
| [Qwen/Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) | 4096 | 262144 | `trl-jobs sft --model_name Qwen/Qwen3-8B --dataset_name ...` |

#### Qwen3 with PEFT

| Model | Maximum context length | # of tokens per effective batch size | Command |
| --- | --- | --- | --- |
| [Qwen/Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) | 24576 | 196608 | `trl-jobs sft --model_name Qwen/Qwen3-8B --peft --dataset_name ...` |
| [Qwen/Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B) | 20480 | 163840 | `trl-jobs sft --model_name Qwen/Qwen3-14B --peft --dataset_name ...` |
| [Qwen/Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) | 4096 | 131072 | `trl-jobs sft --model_name Qwen/Qwen3-32B --peft --dataset_name ...` |

## Authentication

You can provide your Hugging Face token in several ways:

1. Using `huggingface-hub` login: `huggingface-cli login`
2. Setting the `HF_TOKEN` environment variable
3. Using the `--token` argument

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

Run command to check and format code:

```sh
ruff check . --fix && ruff format . --line-length 119
```
