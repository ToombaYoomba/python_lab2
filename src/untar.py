import tarfile
from src.check_path import check_path

def untar(current_path, data):
    """
    Разархивация указанного tar.gz файла

    Открывает указанный tar.gz файл и достаёт из него содержимое
    Место разархивации - текущий каталог
    """
    tar_file = data[0]

    tar_data = check_path(current_path, tar_file)
    tar_path = tar_data[1]

    if tar_data[0] in ["f./", "frec", "fabs"]:
        with tarfile.open(tar_path, "r:gz") as tar:
            tar.extractall(current_path)

        print(f"Extracted tar.gz file {tar_file} to current directory")

    else:
        print("ERROR: tar.gz file not found")