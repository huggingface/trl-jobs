# 🏭 TRL Jobs

**TRL Jobs** is a simple wrapper around [`hfjobs`](https://huggingface.co/docs/huggingface_hub/guides/jobs) that makes it easy to run [TRL](https://huggingface.co/docs/trl/) (Transformer Reinforcement Learning) workflows directly on 🤗 Hugging Face infrastructure.

Think of it as the quickest way to kick off **Supervised Fine-Tuning (SFT)** and more, without worrying about all the boilerplate setup.

## 📦 Installation

Get started with a single command:

```bash
pip install trl-jobs
```

## ⚡ Quick Start

Run your first supervised fine-tuning job in just one line:

```bash
trl-jobs sft --model_name Qwen/Qwen3-0.6B --dataset_name trl-lib/Capybara
```

Th training is tracked with [Trackio](https://huggingface.co/docs/trackio/index) and the fine-tuned model is automatically pushed to the Hub.

<div style="display: flex; flex-wrap: wrap; gap: 10px; align-items: flex-start;">
  <img src="https://huggingface.co/datasets/trl-lib/documentation-images/resolve/main/trackio_sft.gif" alt="trackio_sft" style="max-width: 48%; height: auto;">
  <img src="https://huggingface.co/datasets/trl-lib/documentation-images/resolve/main/trained_model_sft.png" alt="trained_model_sft" style="max-width: 48%; height: auto;">
</div>

## 🛠 Available Commands

Right now, **SFT (Supervised Fine-Tuning)** is supported. More workflows will be added soon!

### 🔹 SFT (Supervised Fine-Tuning)

```bash
trl-jobs sft --model_name Qwen/Qwen3-0.6B --dataset_name trl-lib/Capybara
```

#### Required arguments

* `--model_name` → Model to fine-tune (e.g. `Qwen/Qwen3-0.6B`)
* `--dataset_name` → Dataset to train on (e.g. `trl-lib/Capybara`)

#### Optional arguments

* `--peft` → Use [PEFT (LoRA)](https://huggingface.co/docs/peft) (default: `False`)
* `--flavor` → Hardware flavor (default: `a100-large`, only option for now)
* `--timeout` → Max runtime (`1h` by default). Supports `s`, `m`, `h`, `d`
* `-d, --detach` → Run in background and print job ID
* `--namespace` → Namespace where the job will run (default: your user namespace)
* `--token` → Hugging Face token (only needed if not logged in)

➡️ You can also pass **any arguments supported by `trl sft`**. For the full list, see the [TRL CLI docs](https://huggingface.co/docs/trl/en/clis).

## 📊 Supported Configurations

Here are some ready-to-go setups you can use out of the box.

### 🦙 Meta LLaMA 3

| Model                                                                                  | Max context length | Tokens / batch | Example command                                                                    |
| -------------------------------------------------------------------------------------- | ------------------ | -------------- | ---------------------------------------------------------------------------------- |
| [Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B)                   | 4096               | 262,144        | `trl-jobs sft --model_name meta-llama/Meta-Llama-3-8B --dataset_name ...`          |
| [Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) | 4096               | 262,144        | `trl-jobs sft --model_name meta-llama/Meta-Llama-3-8B-Instruct --dataset_name ...` |

#### 🦙 Meta LLaMA 3 with PEFT

| Model                    | Max context length | Tokens / batch | Example command                                                                           |
| ------------------------ | ------------------ | -------------- | ----------------------------------------------------------------------------------------- |
| Meta-Llama-3-8B          | 24,576             | 196,608        | `trl-jobs sft --model_name meta-llama/Meta-Llama-3-8B --peft --dataset_name ...`          |
| Meta-Llama-3-8B-Instruct | 24,576             | 196,608        | `trl-jobs sft --model_name meta-llama/Meta-Llama-3-8B-Instruct --peft --dataset_name ...` |

### 🐧 Qwen3

| Model                                                | Max context length | Tokens / batch | Example command                                                |
| ---------------------------------------------------- | ------------------ | -------------- | -------------------------------------------------------------- |
| [Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) | 32,768             | 65,536         | `trl-jobs sft --model_name Qwen/Qwen3-0.6B --dataset_name ...` |
| [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) | 24,576             | 98,304         | `trl-jobs sft --model_name Qwen/Qwen3-1.7B --dataset_name ...` |
| [Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B)     | 20,480             | 163,840        | `trl-jobs sft --model_name Qwen/Qwen3-4B --dataset_name ...`   |
| [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B)     | 4,096              | 262,144        | `trl-jobs sft --model_name Qwen/Qwen3-8B --dataset_name ...`   |

#### 🐧 Qwen3 with PEFT

| Model     | Max context length | Tokens / batch | Example command                                                      |
| --------- | ------------------ | -------------- | -------------------------------------------------------------------- |
| Qwen3-8B  | 24,576             | 196,608        | `trl-jobs sft --model_name Qwen/Qwen3-8B --peft --dataset_name ...`  |
| Qwen3-14B | 20,480             | 163,840        | `trl-jobs sft --model_name Qwen/Qwen3-14B --peft --dataset_name ...` |
| Qwen3-32B | 4,096              | 131,072        | `trl-jobs sft --model_name Qwen/Qwen3-32B --peft --dataset_name ...` |

### 🤖 OpenAI GPT-OSS (with PEFT)

🚧 Coming soon!

💡 Want support for another model? Open an issue or submit a PR—we’d love to hear from you!

## 🔑 Authentication

You’ll need a Hugging Face token to run jobs. You can provide it in any of these ways:

1. Login with `huggingface-cli login`
2. Set the environment variable `HF_TOKEN`
3. Pass it directly with `--token`

## 📜 License

This project is under the **MIT License**. See the [LICENSE](./LICENSE) file for details.

## 🤝 Contributing

We welcome contributions!
Please open an issue or a PR on GitHub.

Before committing, run formatting checks:

```bash
ruff check . --fix && ruff format . --line-length 119
```
