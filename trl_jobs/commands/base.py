from abc import ABC, abstractmethod
from argparse import _SubParsersAction, Namespace
import subprocess
import sys


class BaseTRLCommand(ABC):
    """Base class for TRL commands that wrap hfjobs functionality."""

    def __init__(self, args: Namespace) -> None:
        self.args = args
        self.flavor = getattr(args, "flavor", "t4-small")
        self.token = getattr(args, "token", None)
        self.detach = getattr(args, "detach", False)

    @staticmethod
    @abstractmethod
    def register_subcommand(parser: _SubParsersAction) -> None:
        """Register the command with the argument parser."""
        pass

    @abstractmethod
    def get_command_args(self) -> list[str]:
        """Return the command arguments to pass to the container."""
        pass

    def run(self) -> None:
        """Execute the hfjobs run command with the appropriate parameters."""
        # Build the hfjobs command
        hfjobs_cmd = ["hfjobs", "run", "--flavor", self.flavor]

        # Add token if provided
        if self.token:
            hfjobs_cmd.extend(["--token", self.token])

        # Add detach flag if set
        if self.detach:
            hfjobs_cmd.append("--detach")

        # Add Docker image/space
        hfjobs_cmd.append("hf.co/spaces/trl-lib/train")

        # Add command arguments
        hfjobs_cmd.extend(self.get_command_args())

        # Print the command being executed (for debugging)
        print(f"Executing: {' '.join(hfjobs_cmd)}")

        # Execute the command
        try:
            subprocess.run(hfjobs_cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing hfjobs command: {e}")
            sys.exit(e.returncode)
        except FileNotFoundError:
            print("Error: hfjobs command not found. Make sure hfjobs is installed.")
            sys.exit(1)
