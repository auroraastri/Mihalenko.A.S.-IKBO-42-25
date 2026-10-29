def parse_command(command_line: str) -> list[str]:

    cleaned_line = command_line.strip()
    if not cleaned_line:
        return []
    return cleaned_line.split()
