# optai

Optai is a python based command-line tool designed to optimize and enhance your python repositories by rewriting your functions in a cleaner and more optimised way.
It helps improve the readability, performance, and maintainability of Python code by applying various transformations.

This is based on the OpenAI LLM and requires you to have an API key.

## Features

- Automatically optimize and clean Python code in a given repository.
- Improve variable naming, formatting, and code structure.
- Easily integrate with your Python projects for code enhancement.

## Setup

1. Clone the Python Code Optimizer repository:

   ```bash
   git clone git@github.com:IlluvatarEru/optai.git

2. Install requirements:
    
    ```bash
    pip install -r requirements.txt

3. Add your OpenAI key and organisation to the `.env` file:

   ```bash
   echo 'export OPEN_AI_KEY="YOUR_KEY"' >> .env

   echo 'export OPEN_AI_ORG="YOUR_ORGA"'>> .env

4. Add Optai to `bashrc`:

   ```bash
   OPTAI_PATH=$(pwd)
   echo 'alias optai="$OPTAI_PATH/optai.bash"' >> ~/.bashrc
   echo 'export OPTAI_PATH=$OPTAI_PATH'>> ~/.bashrc
   source ~/.bashrc

5. Run on a target repo:

    ```bash
   optai "path_to_repo"
   ```
Flags:
   - You can add the flag `--opti-only` to ask it to just optimize the performance of the code rather than to also improve the variable naming, formatting etc.
   - You can add the flag `--file=<file_name>` to ask it to only process a single file

## What's next?
We plan on: 
- enabling this repo to work on most languages
- rewriting it in rust so that it is faster
- improving the rewriting quality
- making it work with local models rather than only OpenAI