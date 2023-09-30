def parse_cmd(s: str):

    parts = s.split()
    if not parts:
        return "", []

    command = parts[0]
    parameters = parts[1:]
    return command, parameters