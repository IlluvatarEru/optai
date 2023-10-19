import argparse
import os

from logging_utils import log_text, logger
from optimizer import rewrite_file_with_open_ai


def main():
    try:
        parser = argparse.ArgumentParser(description="Python Code Optimizer")
        parser.add_argument("repo_path", help="Path to the Python repository to optimize")
        args = parser.parse_args()
        log_text(f"Rewriting code for repo: {args.repo_path}")

        if os.path.isdir(args.repo_path):
            for root, _, files in os.walk(args.repo_path):
                for file in files:
                    if file.endswith(".py"):
                        file_path = os.path.join(root, file)
                        rewrite_file_with_open_ai(file_path)
    except Exception as e:
        logger.exception(e)


if __name__ == "__main__":
    main()
