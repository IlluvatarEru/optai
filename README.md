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

5. Run on a target repo:

    ```bash
    pip install -r requirements.txt
