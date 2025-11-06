import zipfile

from src.check_path import check_path
from src.constants import FuncError


def unzip(current_path, data):
    """
    Разархивация указанного zip файла

    Открывает указанный zip файл и достаёт из него содержимое
    Место разархивации - текущий каталог
    """
    zip_file = data[0]

    zip_data = check_path(current_path, zip_file)
    zip_path = zip_data[1]

    if zip_data[0] in ["f./", "frec", "fabs"]:
        with zipfile.ZipFile(zip_path, "r") as zipf:
            zipf.extractall(current_path)

        print(f"Extracted zip file {zip_file} to current directory")

    else:
        raise FuncError("zip file not found")
