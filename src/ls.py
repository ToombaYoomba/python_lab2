import stat
from datetime import datetime
from os import listdir, scandir

# data = input().split()


def ls(data):
    if len(data) == 0:
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
        print("too many ls arguments")

    if len(file_path) == 0 or len(file_path.strip()) == 0:
        file_path = None

    files = []

    if flag == "-l":
        # print("name  type  size  change_time    permissions")

        contains = scandir(file_path)

        for item in contains:
            print(item)
            file_stats = []

            name = item.name
            file_stats.append(name)

            file_type = None

            if item.is_file():
                file_type = "file"
            elif item.is_dir():
                file_type = "dir"

            file_stats.append(file_type)

            stats = item.stat()

            size = stats.st_size
            file_stats.append(size)

            change_time = datetime.fromtimestamp(stats.st_mtime).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            file_stats.append(change_time)

            permissions = stat.filemode(stats.st_mode)
            file_stats.append(permissions)

            files.append(file_stats)

        # for item in files:

        #     print(item[0], item[1], item[2], item[3])

    else:
        files = listdir(file_path)

        # for item in files:
        #     print(item)

    return files


# print(ls(data))
