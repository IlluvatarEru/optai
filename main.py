import argparse
import os

from logging_utils import log_text, logger
from optimizer import rewrite_file_with_open_ai


def main():
    try:
        parser = argparse.ArgumentParser(description="Python Code Optimizer")
        parser.add_argument(
            "repo_path", help="Path to the Python repository to optimize"
        )
        parser.add_argument(
            "--perf-only", type=str, help="Specify 'true' or 'false' for perf-only"
        )

        args = parser.parse_args()
        repo_path = args.repo_path
        perf_only = args.perf_only
        log_text(
            f"Optimizing code for repository: {repo_path}\n - perf_only: {perf_only}"
        )

        if os.path.isdir(repo_path):
            for root_dir, _, files in os.walk(repo_path):
                for file in (f for f in files if f.endswith(".py")):
                    file_path = os.path.join(root_dir, file)
                    rewrite_file_with_open_ai(
                        file_path, perf_only, language="python"
                    )
    except Exception as err:
        logger.exception(err)


if __name__ == "__main__":
    main()
