import os
import shutil

from src.check_path import check_path
from src.cp import cp

# current_path = getcwd().replace("\\", "/")
# print(f"current path: {current_path}")

# data = input().split()
# print(f"entered data: {data}")


def mv(current_path, data):
    # print(f"data {data}")
    copy_data = data  # входная дата (что двигать и куда)

    files_to_move = copy_data[:-1]  # что двигать
    # print(f"files to move: {files_to_move}")

    destination = copy_data[-1]  # куда двигать
    # print(f"destination: {destination}")
    destination_data = check_path(current_path, destination)
    destination_path = destination_data[1]
    # print(f"destination data: {destination_data}")

    files_paths = []

    if destination_data[0] in ["c", "rec./", "rec", "abs"]:
        new_data = data
        new_data.insert(0, "-r")
        # print(f"new data {new_data}")
        cp(current_path, new_data)
        for item in files_to_move:
            # print(f"item {item}")
            item_path = check_path(current_path, item)[1]
            files_paths.append(item_path)
            if os.path.isfile(item_path):
                os.remove(item_path)
            else:
                shutil.rmtree(item_path)

    elif destination_data[0] in ["f./", "frec", "fabs", "newrec", "newabs"]:
        if len(files_to_move) != 1:
            print("too many/few files to move")

        else:
            file = files_to_move[0]
            # print(f"file to move {file}")
            file_data = check_path(current_path, file)
            # print(f"file to move data {file_data}")

            if os.path.isfile(file_data[1]):
                cp(current_path, data)
                os.remove(file_data[1])
            elif file_data[0] in ["c", "rec./", "rec", "abs"]:
                print("can't move dir to file")
            else:
                print(f"moving error {destination_data[0]}")

    meta_data = [files_paths, destination_path]
    return meta_data


# mv(current_path, data)
