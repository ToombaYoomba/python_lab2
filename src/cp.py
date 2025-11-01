import shutil

from src.check_path import check_path

# current_path = getcwd().replace("\\", "/")
# print(f"current path: {current_path}")

# data = input().split()
# print(data)


def cp(current_path, data):
    """
    Копирование файла из источника в назначение

    На вход получает текущий путь и список: флаг,
    файлы для копирования и место куда копировать
    Если получен флаг -r, то может копировать диреткори и их содержимое
    Иначе только файлы
    """
    flag = None
    copy_data = None

    if data[0] == "-r":
        flag = "-r"
        copy_data = data[1:]
    else:
        copy_data = data

    files_to_copy = copy_data[:-1]
    # print(f"file to copy: {files_to_copy}")

    destination = copy_data[-1]
    # print(f"destination: {destination}")
    destination_data = check_path(current_path, destination)
    destination_path = destination_data[1]
    # print(f"destination data: {destination_data}")

    if flag == "-r":
        for item in files_to_copy:
            item_data = check_path(current_path, item)
            item_path = item_data[1]
            # print(f"item data: {item_data}")

            if item_data[0] in ["f./", "frec", "fabs"]:
                shutil.copy2(item_path, destination_path)

            elif item_data[0] in ["c", "rec./", "rec", "abs"]:
                shutil.copytree(
                    item_path, destination_path + "/" + item_path.split("/")[-1]
                )

            else:
                print(
                    f"wtf {item_path, destination_path + '/' + item_path.split('/')[-1]}"
                )

    else:
        for file in files_to_copy:
            path_start_data = check_path(current_path, file)
            if path_start_data[0] in ["f./", "frec", "fabs", "newrec", "newabs"]:
                file_path = path_start_data[1]
                shutil.copy2(file_path, destination_path)
            else:
                print("Trying to copy to many files")


# cp(current_path, data)
