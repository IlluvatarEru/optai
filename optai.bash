#!/bin/bash
path_to_repo=$1
python main.py $path_to_repo
black $path_to_repo