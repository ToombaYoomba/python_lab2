import os

from src.check_path import check_path
from src.constants import FuncError

def grep(current_path, data):
    """
    Поиск строк, соответствующих шаблону в файлах

    На вход получает текущий путь и список:
    флаг, паттерн поиска и файлы/каталоги для поиска
    Возвращает список строк, содержащих нужный паттерн
    Поддержка опции -r рекурсивный поиск в подкаталогах
    Поддержка опции -i поиск без учёта регистра
    Вывод: имя файла, номер строки и найденный фрагмент
    """
    flags = []
    grep_data = None

    if data[0] == "-r" or data[0] == "-i":

        flags.append(data[0])

        if len(data) > 2 and flags[0] == "-r" and data[1] == "-i":
            flags.append("-i")
            if len(data) in [3,4]:
                grep_data = data[2:]
            else:
                raise FuncError("wrong number of arguments")
                return 0
        elif len(data) > 2 and flags[0] == "-i" and data[1] == "-r":
            flags.append("-r")
            if len(data) in [3,4]:
                grep_data = data[2:]
            else:
                raise FuncError("wrong number of arguments")
                return 0
        elif len(data) in [2,3]:
            grep_data = data[1:]
        else:
            raise FuncError("wrong number of arguments")
            return 0
        
    elif data[0] == "-ri" or data[0] == "-ir":
        flags.append("-r")
        flags.append("-i")

        if len(data) in [2,3]:
            grep_data = data[1:]
        else:
            raise FuncError("wrong number of arguments")
            return 0

    elif len(data) in [1,2]:
        grep_data = data

    else:
        raise FuncError("wrong number of arguments")
        return 0
    

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

    result = []

    # print(f"pattern {pattern}")
    # print(f"search path {search_path}")

    if "-r" in flags:
        if search_data[0] in ["c", "rec./", "rec", "abs"]:

            if "-i" in flags:
                pattern = pattern.lower()
                for root, dirs, files in os.walk(search_path):
                    for file in files:
                        file_path = os.path.join(root, file)

                        with open(file_path, 'r') as f:
                            # print(f"file opened")
                            try:
                                for i, line in enumerate(f, 1):
                                    # print(i, line)
                                    if pattern in line.lower():
                                        result.append(f"{file_path} {i}: {line.strip()}")
                                        print(f"{file_path} {i}: {line.strip()}")
                            except Exception:
                                pass
            
            else:
                for root, dirs, files in os.walk(search_path):
                    for file in files:
                        file_path = os.path.join(root, file)

                        with open(file_path, 'r') as f:
                            # print(f"file opened")
                            try:
                                for i, line in enumerate(f, 1):
                                    # print(i, line)
                                    if pattern in line:
                                        result.append(f"{file_path} {i}: {line.strip()}")
                                        print(f"{file_path} {i}: {line.strip()}")
                            except Exception:
                                pass


        else:

            raise FuncError(f"path not dir {search_path}")


    else:
        if search_data[0] in ["f./", "frec", "fabs"]:

            if "-i" in flags:
                pattern = pattern.lower()

                with open(search_path, 'r') as f:
                    for i, line in enumerate(f, 1):
                        if pattern in line.lower():
                            result.append(f"{file_path} {i}: {line.strip()}")
                            # print(f"{search_path} {i}: {line.strip()}")

            else:
                with open(search_path, 'r') as f:
                    # print(f"file opened")
                    for i, line in enumerate(f, 1):
                        # print(i, line)
                        if pattern in line:
                            result.append(f"{file_path} {i}: {line.strip()}")
                            # print(f"{search_path} {i}: {line.strip()}")

        else:
            raise FuncError(f"path not file {search_path}")

    return result


