from src.check_path import check_path
from src.find_path import find_path
from src.mv import mv
from src.constants import TRASH_PATH
from src.constants import FuncError
import os
import shutil
import ast

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
    # print(paths_list)

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
            raise FuncError("нельзя удалить исходящую папку при undo для cp")

    else:
        for item_path in paths_list:

            os.remove(item_path)

def unmv(current_path, data):
    files_moved_original = data[0] #откда забрали файлы (имеет их имя)
    current_position = data[1] #где они есть теперь

    for file in files_moved_original:
        try:
            file_name = file.split("/")[-1] #имя
            original_position = file.split("/")[:-1] #изначальная позиция файлов
            original_position = "/".join(original_position)
            mv_data = [file_name, original_position] # список имя и куда двигать
            # print(f"into mv {current_position, mv_data}")
            mv(current_position, mv_data)
        except Exception:
            raise FuncError(f"file not found {file_name}")

def unrm(current_path, data):
    flag = data[0]
    original_paths = data[1]
    # print(original_paths)

    for original_path in original_paths:
        file_dir = "/".join(original_path.split("/")[:-1])
        file_name = os.path.basename(original_path)
        trash_file_path = find_path(TRASH_PATH) + "/" + file_name
        move_data = [trash_file_path, file_dir]

        # print(move_data)

        mv(current_path, move_data)


def undo(current_path):
    """
    Отмена последней команды из списка ср, mv, rm.

    На вход получает только текущий путь
    Последнюю команду берёт из meta.log
    Для ср: удаление скопированного файла/каталога
    Для му: возврат объекта в исходное место
    Для rm: восстановление из временного каталога.trash
    """
    with open("meta.log", "r") as f:
                
        lines = f.readlines()
        try:
            log = lines[-1].strip()
        except Exception:
            raise FuncError("history clear")
            return 0
        
        # print(log)

        command = log.split(" ", maxsplit=3)[3:]
        command = command[0]
        command = ast.literal_eval(command)
        # print(command)
        command_data = command[1]
        command = command[0]
        # print(command)
        # print(command_data)

        if command == "cp":
            uncp(current_path, command_data[0].split())

        elif command == "mv":
            unmv(current_path, command_data)

        elif command == "rm":
            unrm(current_path, command_data)

        else:
            raise FuncError("unknown command")
        
