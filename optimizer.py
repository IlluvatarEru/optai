from logging_utils import log_text
from open_ai import get_answer

DEF_ = "def "


def rewrite_file_with_open_ai(file_path):
    log_text(f"Rewriting {file_path}...")

    with open(file_path, 'r') as file:
        code = file.read()

    functions = [DEF_ + e for e in code.split(DEF_)[1:]]

    for func in functions:
        func = func.split('\nif __name__ == "__main__":')[0]
        log_text(f"base func:\n{func}")

        # Call the OpenAI API to rewrite the function code
        rewritten_func = rewrite_function_with_open_ai(func)
        log_text(rewritten_func)
        log_text("------")
        code = code.replace(func, rewritten_func)

    # Write the optimized code back to the file
    with open(file_path, 'w') as file:
        file.write(code)
    log_text(f"Finished rewriting {file_path}")


def rewrite_function_with_open_ai(code):
    # we keep func names unchanged
    func_name = code.split("(")[0] + "("
    log_text(f"func_name={func_name}")

    messages = [
        {"role": "system", "content": "Please rewrite the following Python code to clean and optimize it."},
        {"role": "user", "content": code},
    ]

    open_ai_answer = get_answer(messages=messages)
    f = open_ai_answer.split(DEF_)[1].split("```")[0] + "\n\n"
    f = f.split("(", 1)[1]

    f = func_name + f

    return f
