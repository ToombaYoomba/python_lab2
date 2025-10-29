import os

def find_path(filename, search_path = None):
    if search_path is None:
        search_path = "."
        for root, dirs, files in os.walk(search_path):
            if filename in dirs:
                file_path = os.path.abspath(filename)
                # print(f"Директория найдена: {file_path}")
                return file_path
    else:

        for root, dirs, files in os.walk(search_path):
            if filename in files:
                file_path = os.path.join(root, filename)
                # print(f"Файл найден: {file_path}")
                return file_path
        
    print(f"Файл '{filename}' не найден.")
    return None