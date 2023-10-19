import re

from logging_utils import log_text
from open_ai import get_answer

DEF_ = "def "
CLASS_ = "class "


def rewrite_file_with_open_ai(file_path, perf_only=False, language="python"):
    log_text(f"Rewriting {file_path}...")

    with open(file_path, "r") as read_file:
        original_content = read_file.read()
        log_text(original_content)

    # Use regular expressions to split code into functions and classes
    function_pattern = re.compile(rf'(def [^\n]+:\n(?:[^\n]+\n)+)', re.MULTILINE)
    class_pattern = re.compile(rf'(class [^\n]+:\n(?:[^\n]+\n)+)', re.MULTILINE)

    # Find all functions and classes in the code
    functions = function_pattern.findall(original_content)
    classes = class_pattern.findall(original_content)
    log_text(f"functions={functions}")

    log_text(f"classes={classes}")
    for func_part in functions:
        func_part = func_part.split('\nif __name__ == "__main__":')[0]
        log_text(f"Base function:\n{func_part}")

        # Use the OpenAI API to rewrite the function code
        revised_func = rewrite_function_with_open_ai(
            func_part, perf_only=perf_only, language=language
        )
        log_text(revised_func)
        log_text("------")
        original_content = original_content.replace(func_part, revised_func)

    for c in classes:
        log_text(f"Base class:\n{func_part}")

        # Use the OpenAI API to rewrite the function code
        revised_class = rewrite_class_with_open_ai(
            c, perf_only=perf_only, language=language
        )
        log_text(revised_func)
        log_text("------")
        original_content = original_content.replace(c, revised_class)

    # Save the optimized code back to the file
    with open(file_path, "w") as write_file:
        write_file.write(original_content)
    log_text(f"Finished rewriting {file_path}")


def get_instructions(perf_only, language="python"):
    mode = (
        "only to optimize performance, leave constants (upper case variables) and function names unchanged."
        if perf_only
        else "optimize performance, tidy up Python code, improve variables naming and formatting, rename variables like myVar to my_var """
    )
    return f"Please rewrite the following {language} code, {mode}"


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


def rewrite_class_with_open_ai(code_block, perf_only=False, language="python"):
    class_declaration = code_block.split(":")[0] + ":"
    instructions = get_instructions(perf_only, language)

    prompts_data = [
        {
            "role": "system",
            "content": instructions,
        },
        {"role": "user", "content": code_block},
    ]

    ai_answer = get_answer(messages=prompts_data)
    log_text(ai_answer)
    modified_code = ""
    try:
        if "```" in ai_answer:
            modified_code = ai_answer.split(CLASS_)[1].split("```\n")[0] + "\n\n"
            modified_code = modified_code.split(":", 1)[1]
            final_code = class_declaration + modified_code
        else:
            final_code = code_block
    except:
        log_text("ERROR")
        log_text(f"Class declaration = {class_declaration}")
        log_text(f"modified_code={modified_code}")
        log_text(f"modified_code_split={modified_code.split(':')}")
        final_code = ""

    return final_code
