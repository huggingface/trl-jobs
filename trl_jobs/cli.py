#!/usr/bin/env python3
"""
TRL Jobs CLI - A wrapper around hfjobs for TRL-specific workflows.
"""

import sys
from argparse import ArgumentParser

from .commands.sft import SFTCommand


def main():
    """Main entry point for trl-jobs CLI."""
    parser = ArgumentParser(
        "trl-jobs",
        description="TRL-specific job runner built on hfjobs",
        usage="trl-jobs <command> [<args>]",
    )

    # Create subparsers for different commands
    commands_parser = parser.add_subparsers(
        title="Available commands", help="TRL job types", dest="command"
    )

    # Register all commands
    SFTCommand.register_subcommand(commands_parser)

    # Parse arguments
    args = parser.parse_args()

    # Check if a command was provided
    if not hasattr(args, "func"):
        parser.print_help()
        print("\nError: No command specified.")
        sys.exit(1)

    # Execute the command
    try:
        service = args.func(args)
        service.run()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
