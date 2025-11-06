import os
from src.constants import AddFuncError

def find_path(filename, search_path = None):
    """
    Поиск пути аналогично check_paths, но без обработки случаев

    На вход получает имя файла/каталога и (опционально) каталог, в котором искать
    Возвращает абсолютный путь к файлу 
    """
    if search_path is None:
        search_path = "."
        for root, dirs, files in os.walk(search_path):
            if filename in dirs:
                # print(filename)
                file_path = os.path.join(root, filename)
                file_path = str(os.path.abspath(file_path))
                # print(f"shit {file_path}")
                file_path = file_path.replace("\\", "/")
                # print(f"Директория найдена: {file_path}")
                return file_path
            
        for root, dirs, files in os.walk(search_path):
            if filename in files:
                # print(filename)
                file_path = os.path.join(root, filename)
                file_path = str(os.path.abspath(file_path))
                # print(f"shit {file_path}")
                file_path = file_path.replace("\\", "/")
                # print(f"Файл найден: {file_path}")
                return file_path
            
    else:

        for root, dirs, files in os.walk(search_path):
            if filename in files:
                file_path = os.path.join(root, filename)
                file_path = "/".join(file_path.split("\\\\"))
                # print(f"Файл найден: {file_path}")
                return file_path
        
    raise AddFuncError(f"Файл '{filename}' не найден.")
    return None