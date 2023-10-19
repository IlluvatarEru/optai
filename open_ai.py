import os

import dotenv
import openai

dotenv.load_dotenv(".env")
openai.api_key = os.environ.get("OPEN_AI_KEY")
openai.organization = os.environ.get("OPEN_AI_ORG")


def get_answer(messages):
    response = openai.ChatCompletion.create(
        # model="gpt-3.5-turbo",
        model="text-davinci-001",
        messages=messages,
    )
    result = response.choices[0].message.content
    return result
