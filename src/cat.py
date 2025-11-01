from src.check_path import check_path

# current_path = getcwd().replace("\\", "/")
# print(f"current path: {current_path}")

# needed_path = input()
# data = check_path(current_path, needed_path)
# print(data)

# if os.path.exists(current_path.replace('\\', '/')):
#     print("yes")
# else:
#     print("no")


def cat(current_path, data):
    """
    Вывод содержимого указанного файла в консоль

    На вход получает текущий путь и название файла/его путь
    Обрабатывает все возможные случаи с путями
    В случае передачи существующего пути открывает файл
    и выводит его содержимое в консоль
    """
    data = check_path(current_path, data)

    if data[0] == "n":
        # print(f"stay in current directory {current_path}")
        pass

    elif data[0] == "b":
        print(f"no path: {data[2]}")

    elif data[0] == "s":
        print(f"no path: {data[2]}")

    elif data[0] in ["c", "rec./", "rec", "abs"]:
        print(f"{data[2]} is not file")

    elif data[0] in ["f./", "frec", "fabs"]:
        with open(data[1], "r", encoding="utf-8") as file:
            content = file.read()
            print(content)

    else:
        pass


# cat(data)
