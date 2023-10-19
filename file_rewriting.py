import argparse

from logging_utils import log_text, logger
from optimizer import rewrite_file_with_open_ai
from utils import str_to_bool


def main():
    log_text("Starting file_rewriting")
    try:
        parser = argparse.ArgumentParser(description="Python Code Optimizer")
        parser.add_argument(
            "repo_path", help="Path to the Python repository to optimize"
        )
        parser.add_argument(
            "--perf-only", type=str, help="Specify 'true' or 'false' for perf-only"
        )
        parser.add_argument(
            "--file-name", type=str, help="Specify the file name to rewrite"
        )

        args = parser.parse_args()
        repo_path = args.repo_path
        perf_only = str_to_bool(args.perf_only)
        file_name = args.file_name

        log_text(
            f"Optimizing code for file: {repo_path}/{file_name}\n - perf_only: {perf_only}"
        )
        f = repo_path + "/" + file_name
        rewrite_file_with_open_ai(f, perf_only, language="python")
    except Exception as err:
        logger.exception(err)


if __name__ == "__main__":
    main()
