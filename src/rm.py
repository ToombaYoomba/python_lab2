import os
import shutil

from src.check_path import check_path

# current_path = getcwd().replace("\\", "/")
# print(f"current path: {current_path}")

# data = input().split()
# print(f"entered data: {data}")


def rm(current_path, data):
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
        print("can't delete catalogue without '-r' option")

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
                for item in copy_data:
                    item_data = check_path(current_path, item)
                    item_path = item_data[1]

                    if os.path.isfile(item_path):
                        os.remove(item_path)
                    else:
                        shutil.rmtree(item_path)

            elif confirmation == "n":
                print("lazy bastard")
            else:
                print("unknown command")

        else:
            print("нельзя удалить исходящую папку")

    else:
        for item in copy_data:
            item_data = check_path(current_path, item)
            item_path = item_data[1]

            os.remove(item_path)


# rm(current_path, data)
