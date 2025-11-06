import os
import shutil
from src.cp import cp

from src.check_path import check_path
from src.find_path import find_path
from src.constants import TRASH_PATH
from src.constants import FuncError

# current_path = getcwd().replace("\\", "/")
# print(f"current path: {current_path}")

# data = input().split()
# print(f"entered data: {data}")


def rm(current_path, data):
    """
    Удаление указанного файла/каталога

    На вход получает текущий путь и список из файлов/каталогов для удаления
    Поддержка опции - для удаления каталога рекурсивно со всем содержимым.
    Подтверждение удаления при попытке удлаения директории
    Нельзя удалить родительскую диреткорию от текущей или корневую
    """
    flag = None
    copy_data = None

    if data[0] == "-r":
        flag = "-r"
        copy_data = data[1:]
    else:
        copy_data = data

    type_list = [check_path(current_path, item)[0] for item in copy_data]

    if (
        any([(item in ["c", "rec./", "rec", "abs"]) for item in type_list])
        and flag != "-r"
    ):
        raise FuncError("can't delete catalogue without '-r' option")

    elif any([(item in ["c", "rec./", "rec", "abs"]) for item in type_list]):
        paths_list = [check_path(current_path, item)[1] for item in copy_data]

        flag_del = False

        for i in range(len(type_list)):
            if paths_list[i] in current_path:
                flag_del = True

        if not flag_del:
            confirmation = input(
                f"Вы точно хотите удалить {len(copy_data)} аргумента? [y/n]: "
            )

            if confirmation == "y":
                item_paths = []
                for item in copy_data:
                    item_data = check_path(current_path, item)
                    item_path = item_data[1]
                    item_paths.append(item_path)

                    if os.path.isfile(item_path):
                        cp(current_path, [item_path, find_path(TRASH_PATH)])
                        os.remove(item_path)
                    else:
                        cp(current_path, ["-r", item_path, find_path(TRASH_PATH)])
                        shutil.rmtree(item_path)

            elif confirmation == "n":
                raise FuncError("lazy bastard")
            else:
                raise FuncError("unknown command")

        else:
            raise FuncError("нельзя удалить исходящую папку")

    else:
        item_paths = []
        for item in copy_data:
            item_data = check_path(current_path, item)
            item_path = item_data[1]
            item_paths.append(item_path)
            cp(current_path, [item_path, find_path(TRASH_PATH)])
            os.remove(item_path)

    try:
        return [flag, item_paths]
    except Exception:
        return None

# rm(current_path, data)
