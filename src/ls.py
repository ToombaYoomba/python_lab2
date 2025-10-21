import stat
from datetime import datetime
from os import listdir, scandir

data = input().split()

file_path = data[0]
if len(data) > 1:
    l_flag = data[1]
else:
    l_flag = None


def ls(file_path, l_flag=None):
    if len(file_path) == 0 or len(file_path.strip()) == 0:
        file_path = None

    if l_flag == "-l":
        print("name  size  change_time    permissions")

        contains = scandir(file_path)

        for item in contains:
            name = item.name

            stats = item.stat()

            size = stats.st_size

            change_time = datetime.fromtimestamp(stats.st_mtime).strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            permissions = stat.filemode(stats.st_mode)

            print(name, size, change_time, permissions)

    else:
        contains = listdir(file_path)

        for item in contains:
            print(item)


ls(file_path, l_flag)
