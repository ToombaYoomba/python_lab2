import os

from src.check_path import check_path

def grep(current_path, data):
    flag = None
    grep_data = None

    if data[0] == "-r":
        flag = "-r"
        grep_data = data[1:]
    elif data[0] == "-i":
        flag = "-i"
        grep_data = data[1:]
    else:
        grep_data = data

    pattern = grep_data[0]
    if len(pattern) > 1:
        if pattern[0] in "\"'" and pattern[-1] in "\"'":
            pattern = pattern[1:-1]


    if len(grep_data) == 2:
        search_place = grep_data[1]
    else:
        search_place = current_path

    search_data = check_path(current_path, search_place)
    search_path = search_data[1]

    # print(f"pattern {pattern}")
    # print(f"search path {search_path}")

    if flag == "-r":
        if search_data[0] in ["c", "rec./", "rec", "abs"]:

            for root, dirs, files in os.walk(search_path):
                for file in files:
                    file_path = os.path.join(root, file)

                    with open(file_path, 'r') as f:
                        # print(f"file opened")
                        try:
                            for i, line in enumerate(f, 1):
                                # print(i, line)
                                if pattern in line:
                                    print(f"{file_path} {i}: {line}")
                        except:
                            pass


        else:

            print(f"path not dir {search_path}")


    else:
        if search_data[0] in ["f./", "frec", "fabs"]:

            if flag == "-i":
                pattern = pattern.lower()

                with open(search_path, 'r') as f:
                    for i, line in enumerate(f, 1):
                        if pattern in line.lower():
                            print(f"{search_path} {i}: {line}")

            else:
                with open(search_path, 'r') as f:
                    print(f"file opened")
                    for i, line in enumerate(f, 1):
                        # print(i, line)
                        if pattern in line:
                            print(f"{search_path} {i}: {line}")

        else:
            print(f"path not file {search_path}")


