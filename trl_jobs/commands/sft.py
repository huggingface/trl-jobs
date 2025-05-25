from argparse import _SubParsersAction, Namespace
from typing import List

from .base import BaseTRLCommand


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

    def get_command_args(self) -> List[str]:
        """Build the SFT command arguments."""
        return ["sft", "--model", self.model, "--dataset", self.dataset]
