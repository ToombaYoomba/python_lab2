import stat
from datetime import datetime
from os import listdir, scandir

from src.check_path import check_path
from src.constants import FuncError

# data = input().split()


def ls(current_path, data):
    """
    Вывод содержимого диреткории

    На вход получает текущий путь и путь к директории
    Если путь к директории не указан, то выводит содержимое текущей
    Поддержка опции –l для подробного отображения 
    """
    if data is None:
        file_path = None
        flag = None
    elif len(data) == 0:
        file_path = None
        flag = None
    elif len(data) == 1:
        if data[0] == "-l":
            flag = "-l"
            file_path = None
        else:
            flag = None
            file_path = data[0]
    elif len(data) == 2:
        flag = data[0]
        file_path = data[1]
    else:
        raise FuncError("too many ls arguments")

    file_path_data = check_path(current_path, file_path)

    # print(file_path_data)

    file_path = check_path(current_path, file_path)[1]

    if file_path_data[0] == "n":
        file_path = current_path

    # print(current_path, file_path)

    files = []

    if file_path_data[0] in ["f./", "frec", "fabs"]:
        raise FuncError("ls path to file")

    elif file_path_data[0] in ["newrec", "newabs"]:
        raise FuncError("ls path to nonexistent directory")

    if flag == "-l":
        # print("name  type  size  change_time    permissions")

        contains = scandir(file_path)

        for item in contains:
            # print(item)
            file_stats = []

            name = item.name
            file_stats.append(name)  # 1

            file_type = None

            if item.is_file():
                file_type = "file"
            elif item.is_dir():
                file_type = "dir"

            file_stats.append(file_type)  # 2

            stats = item.stat()

            size = stats.st_size
            file_stats.append(size)  # 3

            change_time = datetime.fromtimestamp(stats.st_mtime).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            file_stats.append(change_time)  # 4

            permissions = stat.filemode(stats.st_mode)
            file_stats.append(permissions)  # 5

            files.append(file_stats)  # to whole scope

        # for item in files:
        #     print(item[0], item[1], item[2], item[3], item[4])

    else:
        # print(file_path)
        files = listdir(file_path)

        # for item in files:
        #     print(item)

    return files


# print(ls(data))
