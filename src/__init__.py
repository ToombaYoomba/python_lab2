import stat
from datetime import datetime
from os import listdir, scandir



data = input().split()

path = data[0]
if len(data) > 1:
    l_flag = data[1]
else:
    l_flag = None


def ls(path, l_flag=None):
    if len(path) == 0 or len(path.strip()) == 0:
        path = None

    if l_flag == "-l":
        contains = scandir(path)

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
        contains = listdir(path)

        for item in contains:
            print(item)


ls(path, l_flag)