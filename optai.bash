#!/bin/bash

PERF_ONLY=false
perf_only="False"

path_to_repo=$1

# Parse command-line options
while [[ "$#" -gt 0 ]]; do
  case "$1" in
  --perf-only)
    PERF_ONLY=true
    shift
    ;;
  *)
    # Assuming the remaining argument is your "myrepo"
    MY_REPO="$1"
    shift
    ;;
  esac
done

# Check if the --perf-only flag is set
if [ "$PERF_ONLY" = true ]; then
  perf_only="True"
fi

python main.py $path_to_repo --perf-only $perf_only
black $path_to_repo
