from src.check_path import check_path
from src.find_path import find_path
from src.mv import mv
import os
import shutil

def uncp(current_path, data):
    flag = None
    copy_data = None

    if data[0] == "-r":
        flag = "-r"
        copy_data = data[1:]
    else:
        copy_data = data

    destination = find_path(copy_data[-1])
    copy_data = copy_data[:-1]

    type_list = [check_path(current_path, find_path(item, destination))[0] for item in copy_data]
    paths_list = [check_path(current_path, find_path(item, destination))[1] for item in copy_data]
    print(paths_list)

    if any([(item in ["c", "rec./", "rec", "abs"]) for item in type_list]):

        flag_del = False

        for i in range(len(type_list)):
            if paths_list[i] in current_path:
                flag_del = True

        if not flag_del:

            for item_path in paths_list:

                if os.path.isfile(item_path):
                    os.remove(item_path)
                else:
                    shutil.rmtree(item_path)

        else:
            print("нельзя удалить исходящую папку при undo для cp")

    else:
        for item_path in paths_list:

            os.remove(item_path)

def unmv(current_path, data):
    files_moved_original = data[0]
    current_position = data[1]

    for file in files_moved_original:
        try:
            file_name = file.split("/")[-1]
            mv(current_position, file.split("/")[:-1].join("/"))
        except Exception:
            print(f"file not found {file_name}")


def undo(current_path):
    with open("meta.log", "r") as f:
                
        lines = f.readlines()
        try:
            log = lines[-1]
        except Exception:
            print("history clear")
            return 0
        
        print(log)

        command = log.split()[3:]

        print(command)

        if command[0] == "cp":
            uncp(current_path, command[1:])

        elif command[0] == "mv":
            unmv(current_path, command[1:])

        else:
            print("unknown command")
        
