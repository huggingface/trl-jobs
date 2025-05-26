import json
from argparse import Namespace, _SubParsersAction
from importlib.resources import files

import yaml
from huggingface_hub.utils import get_token_to_send

from .base import BaseTRLCommand

CONFIGS = {
    ("Qwen/Qwen3-0.6B", "t4-small"): "Qwen3-0.6B-t4-small.yaml",
}


class SFTCommand(BaseTRLCommand):
    """Supervised Fine-Tuning command for TRL."""

    @staticmethod
    def register_subcommand(parser: _SubParsersAction) -> None:
        sft_parser = parser.add_parser("sft", help="Run Supervised Fine-Tuning job")

        # Required arguments
        sft_parser.add_argument(
            "--model",
            type=str,
            required=True,
            help="Model name or path (e.g., Qwen/Qwen3-4B-Base)",
        )
        sft_parser.add_argument(
            "--dataset",
            type=str,
            required=True,
            help="Dataset name or path (e.g., trl-lib/tldr)",
        )

        # Optional arguments
        sft_parser.add_argument(
            "--flavor",
            type=str,
            default="t4-small",
            help="Hardware flavor (default: t4-small)",
        )
        sft_parser.add_argument(
            "--token",
            type=str,
            help="A User Access Token generated from https://huggingface.co/settings/tokens",
        )
        sft_parser.add_argument(
            "-d",
            "--detach",
            action="store_true",
            help="Run the job in the background and print the job ID",
        )

        sft_parser.set_defaults(func=SFTCommand)

    def __init__(self, args: Namespace) -> None:
        super().__init__(args)
        self.model = args.model
        self.dataset = args.dataset

    def get_command_args(self) -> list[str]:
        """Build the SFT command arguments."""
        # Check if the requested configuration exists
        if (self.model, self.flavor) in CONFIGS:
            config_file = CONFIGS[(self.model, self.flavor)]
        else:
            raise ValueError(
                f"No configuration file found for model {self.model} and flavor {self.flavor}"
            )

        # Load YAML file
        config_file = files("trl_jobs.configs").joinpath(config_file)
        with open(config_file, "r") as f:
            args_dict = yaml.safe_load(f)

        # Convert to CLI-style args, ensuring complex structures are JSON-encoded
        cli_args = []
        for k, v in args_dict.items():
            if isinstance(v, (dict, list, bool, type(None))):
                # Serialize complex types and booleans to JSON-compatible format
                v_str = json.dumps(v)
            else:
                v_str = str(v)
            cli_args.extend([f"--{k}", v_str])

        # Get the token
        token = get_token_to_send(self.token)

        return ["trl", "sft"] + cli_args + ["--hub_token", token]
