def write_file(file_name, file_content):
    file_name_with_extension = str(file_name) + ".txt"
    with open(file_name_with_extension, mode="w", encoding="utf-8") as log_file:
        log_file.write(file_content)


def append_file(file_name, append_content):
    file_name_with_extension = str(file_name) + ".txt"
    with open(file_name_with_extension, mode="a", encoding="utf-8") as log_file:
        log_file.write(append_content)


def read_file(file_name):
    file_name_with_extension = str(file_name) + ".txt"
    with open(file_name_with_extension, encoding="utf-8") as text_file:
        return text_file.read()
