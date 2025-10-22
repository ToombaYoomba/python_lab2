from os import getcwd

from src.check_path import check_path

current_path = getcwd().replace("\\", "/")
print(f"current path: {current_path}")

needed_path = input().split("/")
data = check_path(current_path, needed_path)
print(data)

# if os.path.exists(current_path.replace('\\', '/')):
#     print("yes")
# else:
#     print("no")


def cd(data, current_path):
    if data[0] == "n":
        print(f"stay in current directory {current_path}")
        # pass

    elif data[0] == "b":
        current_path = data[1]
        print(f"go back to {current_path}")

    elif data[0] == "s":
        current_path = data[1]
        print(f"go to source directory {current_path}")

    elif data[0] == "c":
        print(f"stay in current directory {current_path}")

    elif data[0] == "rec./":
        current_path = data[1]
        print(f"new path from current by './': {current_path}")

    elif data[0] == "rec":
        current_path = data[1]
        print(f"new path from current: {current_path}")

    elif data[0] == "abs":
        current_path = data[1]
        print(f"new path absolute: {current_path}")

    elif data[0] in ["f./", "frec", "fabs"]:
        print(f"can't move to file {data[2]}")

    elif data[0] == "e":
        pass

    else:
        print("bad case in cd")

    return current_path


cd(data, current_path)
