#!/bin/bash
source ~/.bashrc
PERF_ONLY=false
perf_only="False"
file_name=""

path_to_repo=$1

# Parse command-line options
while [[ "$#" -gt 0 ]]; do
  case "$1" in
  --perf-only)
    PERF_ONLY=true
    shift
    ;;

  --file=*)
      file_name="${1#--file=}"
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

# Check if a file name was provided
if [ -n "$file_name" ]; then
  echo "File Name: $file_name"
fi

if [ -n "$file_name" ]; then
  python $OPTAI_PATH/file_rewriting.py $path_to_repo --perf-only $perf_only --file-name $file_name
else
  python $OPTAI_PATH/main.py $path_to_repo --perf-only $perf_only
  black $path_to_repo
fi