import os
import shutil
from os import getcwd

from src.cat import cat
from src.cd import cd
from src.constants import MainError
from src.cp import cp
from src.grep import grep
from src.history import history
from src.log import log, meta, setup_loggers
from src.ls import ls
from src.mv import mv
from src.rm import rm
from src.tar import tar
from src.undo import undo
from src.untar import untar
from src.unzip import unzip
from src.zip import zip


def main() -> None:
    current_path = getcwd().replace("\\", "/")
    # print(f"current path: {current_path}")

    flag = True
    setup_loggers()
    try:
        os.mkdir("trash")
    except Exception:
        shutil.rmtree("trash")
        os.mkdir("trash")

    while flag:
        error = None

        print(f"\n{current_path}    ₍^. .^₎⟆")

        input_data = input("$ ")

        if len(input_data) == 0 or len(input_data) == 0:
            pass

        else:
            command = input_data.split()[0]

            if len(input_data.split()) > 1:
                command_data = input_data.split()[1:]
            else:
                command_data = None

            # print(f"command {command}")
            # print(f"command data {command_data}")

            # if True:
            try:
                if command == "ls":
                    files = ls(current_path, command_data)

                    for file in files:
                        print(*file)

                    log("i", input_data)

                elif command == "cd":
                    if command_data is None:
                        error = "not enough arguments for cd"
                        raise MainError(error)

                    elif len(command_data) > 1:
                        error = "too many arguments for cd"
                        raise MainError(error)

                    else:
                        current_path = cd(current_path, command_data[0])

                        log("i", input_data)

                elif command == "cat":
                    if command_data is None:
                        result = cat(current_path, command_data)

                        print(result)

                        log("i", input_data)

                    elif len(command_data) > 1:
                        error = "too many arguments for cat"
                        raise MainError(error)

                    else:
                        result = cat(current_path, command_data[0])

                        print(result)

                        log("i", input_data)

                elif command == "cp":
                    if command_data is None:
                        error = "not enough arguments for cp"
                        raise MainError(error)

                    else:
                        cp(current_path, command_data)

                        log("i", input_data)
                        meta(command, input_data.split(" ", maxsplit=1)[1:])

                elif command == "mv":
                    if command_data is None:
                        error = "not enough arguments for mv"
                        raise MainError(error)

                    else:
                        meta_data = mv(current_path, command_data)

                        log("i", input_data)
                        meta(command, meta_data)

                elif command == "rm":
                    if command_data is None:
                        error = "not enough arguments for rm"
                        raise MainError(error)

                    else:
                        meta_data = rm(current_path, command_data)

                        log("i", input_data)
                        meta(command, meta_data)

                elif command == "zip":
                    if command_data is None:
                        error = "not enough arguments for zip"
                        raise MainError(error)

                    elif len(command_data) != 2:
                        error = "wrong number of arguments for zip"
                        raise MainError(error)

                    else:
                        zip(current_path, command_data)

                        log("i", input_data)

                elif command == "unzip":
                    if command_data is None:
                        error = "not enough arguments for unzip"
                        raise MainError(error)

                    elif len(command_data) != 1:
                        error = "wrong number of arguments for unzip"
                        raise MainError(error)

                    else:
                        unzip(current_path, command_data)

                        log("i", input_data)

                elif command == "tar":
                    if command_data is None:
                        error = "not enough arguments for tar"
                        raise MainError(error)

                    elif len(command_data) != 2:
                        error = "wrong number of arguments for tar"
                        raise MainError(error)

                    else:
                        tar(current_path, command_data)

                        log("i", input_data)

                elif command == "untar":
                    if command_data is None:
                        error = "not enough arguments for untar"
                        raise MainError(error)

                    elif len(command_data) != 1:
                        error = "wrong number of arguments for untar"
                        raise MainError(error)

                    else:
                        untar(current_path, command_data)

                        log("i", input_data)

                elif command == "grep":
                    if command_data is None:
                        error = "not enough arguments for grep"
                        raise MainError(error)

                    elif len(command_data) < 1:
                        error = "wrong number of arguments for grep"
                        raise MainError(error)

                    else:
                        result = grep(current_path, command_data)

                        for item in result:
                            print(item)

                        log("i", input_data)

                elif command == "history":
                    if command_data is None:
                        result = history(command_data)

                        for item in result:
                            print(item)

                    elif len(command_data) > 1:
                        error = "wrong number of arguments for history"

                        raise MainError(error)

                    else:
                        result = history(command_data[0])

                        for item in result:
                            print(item)

                elif command == "undo":
                    undo(current_path)

                elif command == "q":
                    flag = False
                    print("\n ---PROGRAM CLOSED--- \n")

                    with open("shell.log", "w", encoding="utf-8"):
                        pass

                    with open("meta.log", "w", encoding="utf-8"):
                        pass

                    shutil.rmtree("trash")

                else:
                    error = f"unknown command {input_data}"
                    raise MainError(error)

            except Exception as error:
                log("e", str(error))
                with open("shell.log", "r") as f:
                    print(f.readlines()[-1].strip())


if __name__ == "__main__":
    main()
