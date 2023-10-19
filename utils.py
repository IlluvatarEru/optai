def str_to_bool(s):
    if s in ["False", "false"]:
        return False
    elif s in ["True", "true"]:
        return True
    else:
        raise Exception(f"Tried to convert {s} to bool")
