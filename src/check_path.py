import os
from src.constants import AddFuncError

# current_path = getcwd().replace("\\", "/")
# print(current_path)

# needed_path = input().split("/")
# print(needed_path)


def check_path(current_path, needed_path):
    """
    Функция для проверки введённого пути и создания абсолютного по нему

    На вход получает текущий путь и путь на проверку
    Обрабатывает все возможные случаи с путями
    Возвращает новый путь в форме абсолютного
    """
    case = None
    buffer_path = None
    enter_path = needed_path

    if needed_path is None:
        pass
    else:
        needed_path = needed_path.split("/")

    # print(needed_path)

    if needed_path is None:
        case = "n"  # no path
        buffer_path = None

    elif len(needed_path[0].strip()) == 0 or len(needed_path[0]) == 0:
        case = "n"  # no path
        buffer_path = None

    elif needed_path[0] == "..":
        case = "b"  # back path

        new_path = "/".join(current_path.split("/")[:-1])

        if os.path.exists(new_path):
            buffer_path = new_path

        else:
            raise AddFuncError("Error bad path ..")
            case = "e"

    elif needed_path[0] == "~":
        case = "s"  # home path
        buffer_path = os.path.expanduser("~")

    elif needed_path[0] == ".":
        # ./None case = c = current

        if len(needed_path[1].strip()) == 0 or len(needed_path[1]) == 0:
            # print(f"Stay in current directory {current_path}")
            case = "c"  # stay in current path with ./
            buffer_path = current_path

        else:  # ./some case
            case = "rec./"  # got rec ./

            new_path = current_path + "/" + "/".join(needed_path[1:])
            if os.path.exists(new_path):
                if os.path.isfile(new_path):
                    case = "f./"  # go to file rec ./
                buffer_path = new_path
                # print(f"new path from current ./: {buffer_path}")

            else:
                raise AddFuncError(f"Error bad path ./{enter_path}")
                case = "e"

    # directories = [item.name for item in scandir(current_path) if item.is_dir()]
    # print(directories)

    else:
        added_path = "/".join(needed_path)

        new_path = current_path + "/" + "/".join(needed_path)

        if os.path.exists(new_path):  # is rec
            if os.path.isfile(new_path):
                case = "frec"  # go to file rec
            else:
                case = "rec"  # go rec
            buffer_path = new_path

        elif os.path.exists(added_path):  # is abs
            if os.path.isfile(added_path):
                case = "fabs"  # go to file abs
            else:
                case = "abs"  # go abs
            buffer_path = added_path

        elif os.path.exists("/".join(new_path.split("/")[:-1])):
            case = "newrec"
            buffer_path = new_path

        elif os.path.exists("/".join(added_path.split("/")[:-1])):
            case = "newabs"
            buffer_path = added_path

        else:
            (f"Error bad path not found {enter_path}")
            case = "e"

    return [case, buffer_path, enter_path]


# print(check_path(needed_path))
