import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    if parts[0] != "mv":
        return

    file_name = parts[1]
    dir_file_name = parts[2]

    directory = os.path.dirname(dir_file_name)

    if dir_file_name[-1] == "/":
        dir_file_name += file_name

    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(file_name, "r") as file_in:
        old_content = file_in.read()

    with open(dir_file_name, "w") as file_out:
        file_out.write(old_content)

    return os.remove(file_name)
