import os
from os import getcwd, scandir

current_path = getcwd().replace("\\", "/")
print(current_path)

needed_path = input().split("/")
print(needed_path)


def check_path(needed_path=None):
    case = None
    buffer_path = None

    if (
        needed_path is None
        or len(needed_path[0].strip()) == 0
        or len(needed_path[0]) == 0
    ):
        case = "n"
        buffer_path = None

    elif needed_path[0] == "..":
        case = "b"

        new_path = "/".join(current_path.split("/")[:-1])

        if os.path.exists(new_path):
            buffer_path = new_path

        else:
            print("Error bad path ..")

    elif needed_path[0] == "~":
        case = "s"
        buffer_path = os.path.expanduser("~")

    elif needed_path[0] == ".":
        # ./None case = c = current

        if len(needed_path[1].strip()) == 0 or len(needed_path[1]) == 0:
            # print(f"Stay in current directory {current_path}")
            case = "c"
            buffer_path = current_path

        else:  # ./some case
            case = "rec./"

            new_path = current_path + "/" + "/".join(needed_path[1:])
            if os.path.exists(new_path):
                if os.path.isfile(new_path):
                    case = "f./"
                buffer_path = new_path
                # print(f"new path from current ./: {buffer_path}")

            else:
                print(f"Error bad path ./{'/'.join(needed_path[1:])}")

    else:
        directories = [item.name for item in scandir(current_path) if item.is_dir()]
        # print(directories)

        added_path = "/".join(needed_path)

        # от текущего
        if needed_path[0] in directories:
            new_path = current_path + "/" + "/".join(needed_path)
            if os.path.exists(new_path):
                if os.path.isfile(new_path):
                    case = "frec"
                else:
                    case = "rec"
                buffer_path = new_path
            else:
                print(f"Error bad path ./{'/'.join(needed_path[1:])}")

        # абсолютный путь
        elif os.path.exists(added_path):
            if os.path.isfile(new_path):
                case = "fabs"
            else:
                case = "abs"
            buffer_path = added_path

        else:
            print(f"Error bad path not found {'/'.join(needed_path[1:])}")

    return [case, buffer_path]


print(check_path(needed_path))
