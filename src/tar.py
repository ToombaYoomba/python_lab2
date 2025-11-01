import os
import tarfile
from src.check_path import check_path

def tar(current_path, data):
    """
    Создание tar.gz архива указанного каталога

    Создаёт tar.gz архив
    В архив записывает путь к файлу директории
    и его относительный путь от архивируемого каталога
    Это нужно для сохранения структуры каталога в архиве
    """
    dir = data[0]
    tar_name = data[1]

    dir_data = check_path(current_path, dir)
    dir_path = dir_data[1]

    if dir_data[0] in ["f./", "frec", "fabs"]:
        tar_data = check_path(current_path, tar_name)
        tar_path = tar_data[1]

        with tarfile.open(tar_path, 'w:gz') as tar:

            dir_name = dir_path.split("/")[-1]
            
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(root, file)  # путь файла

                    relative_path = os.path.relpath(file_path, dir_path)  # относит. путь от архивируемой директории до файла
                    arcname = os.path.join(dir_name, relative_path)  # путь в архиве с корневой папкой

                    tar.add(file_path, arcname)

        print(f"Created tar.gz file {tar_name} from dir {dir}")

    else:
        print("ERROR: dir not found")