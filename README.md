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
trl-jobs sft --flavor a100-large --model Qwen/Qwen3-0.6B --dataset trl-lib/Capybara
```

#### Required Arguments

- `--model`: Model name or path (e.g., `Qwen/Qwen3-0.6B`)
- `--dataset`: Dataset name or path (e.g., `trl-lib/Capybara`)

#### Optional Arguments

- `--flavor`: Hardware flavor (default: `t4-small`)
- `-d, --detach`: Run job in background and print job ID
- `--token`: Hugging Face access token

## Authentication

You can provide your Hugging Face token in several ways:

1. Using `huggingface-hub` login: `huggingface-cli login`
2. Setting the `HF_TOKEN` environment variable
3. Using the `--token` argument

## License

MIT License - see LICENSE file for details.
