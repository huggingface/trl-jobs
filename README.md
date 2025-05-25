# TRL Jobs

A convenient wrapper around `hfjobs` for running TRL (Transformer Reinforcement Learning) specific workflows on Hugging Face infrastructure.

## Installation

```bash
pip install trl-jobs
```

## Available Commands

### SFT (Supervised Fine-Tuning)

Run SFT job with ease:

```bash
trl-jobs sft --model MODEL_NAME --dataset DATASET_NAME [OPTIONS]
```

#### Required Arguments

- `--model`: Model name or path (e.g., `Qwen/Qwen3-4B-Base`)
- `--dataset`: Dataset name or path (e.g., `trl-lib/tldr`)

#### Optional Arguments

- `--flavor`: Hardware flavor (default: `t4-small`)
- `-d, --detach`: Run job in background and print job ID
- `--token`: Hugging Face access token

#### Examples

```bash
trl-jobs sft \
    --model Qwen/Qwen3-4B-Base \
    --dataset trl-lib/tldr
```

## Hardware Flavors

Common hardware flavors you can use:

- `t4-small`: NVIDIA T4 GPU (default)
- `t4-medium`: NVIDIA T4 GPU with more resources
- `a10g-small`: NVIDIA A10G GPU
- `a10g-large`: NVIDIA A10G GPU with more resources
- `a100-large`: NVIDIA A100 GPU

## Authentication

You can provide your Hugging Face token in several ways:

1. Using `huggingface-hub` login: `huggingface-cli login`
2. Setting the `HF_TOKEN` environment variable
3. Using the `--token` argument

## License

MIT License - see LICENSE file for details.
