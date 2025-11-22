import os


def read_all_lines():
    all_lines = []
    input_files_list = os.listdir("data/input/")

    for filename in input_files_list:
        filepath = os.path.join("data/input", filename)
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(lines)
    return all_lines
