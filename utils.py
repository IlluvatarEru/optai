import ast


def pretty_print_code(code):
    # Parse the code and pretty-print it for readability
    parsed_code = ast.parse(code)
    print(ast.dump(parsed_code, indent=4))
