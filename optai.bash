#!/bin/bash
PERF_ONLY=false
path_to_repo=$1
echo $path_to_repo
echo $2

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
  echo "Perf only flag is set."
fi

python main.py $path_to_repo $PERF_ONLY
black $path_to_repo