from logging_utils import log_text
from open_ai import get_answer

DEF_ = "def "


def rewrite_file_with_open_ai(file_path, perf_only=False, language="python"):
    log_text(f"Rewriting {file_path}...")

    with open(file_path, "r") as read_file:
        original_content = read_file.read()

    function_parts = [
        DEF_ + part for part in original_content.split(DEF_)[1:] if len(part) > 10
    ]

    for func_part in function_parts:
        func_part = func_part.split('\nif __name__ == "__main__":')[0]
        log_text(f"Base function:\n{func_part}")

        # Use the OpenAI API to rewrite the function code
        revised_func = rewrite_function_with_open_ai(
            func_part, perf_only=perf_only, language=language
        )
        log_text(revised_func)
        log_text("------")
        original_content = original_content.replace(func_part, revised_func)

    # Save the optimized code back to the file
    with open(file_path, "w") as write_file:
        write_file.write(original_content)
    log_text(f"Finished rewriting {file_path}")


def get_instructions(perf_only, language="python"):
    if perf_only:
        instructions = f"Please rewrite the following {language} code, only to optimize performance. Leave all naming unchanged."
    else:
        instructions = f"Please rewrite the following {language} code, optimize performance, tidy up Python code, improve variable naming and formatting. Leave constants (upper case variables) and function names unchanged."
    return instructions


def rewrite_function_with_open_ai(code_block, perf_only=False, language="python"):
    function_declaration = code_block.split("(")[0] + "("
    log_text(f"Function declaration = {function_declaration}")
    instructions = get_instructions(perf_only, language)

    prompts_data = [
        {
            "role": "system",
            "content": instructions,
        },
        {"role": "user", "content": code_block},
    ]

    ai_answer = get_answer(messages=prompts_data)
    modified_code = ai_answer.split(DEF_)[1].split("```\n")[0] + "\n\n"
    modified_code = modified_code.split("(", 1)[1]

    final_code = function_declaration + modified_code

    return final_code
