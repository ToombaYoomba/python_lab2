from os import getcwd

from src.cat import cat
from src.cd import cd
from src.cp import cp
from src.grep import grep
from src.history import history
from src.ls import ls
from src.mv import mv
from src.rm import rm
from src.tar import tar
from src.untar import untar
from src.unzip import unzip
from src.zip import zip
from src.log import setup_loggers, log, meta
from src.undo import undo



def main() -> None:
    current_path = getcwd().replace("\\", "/")
    # print(f"current path: {current_path}")
    meta(current_path)

    flag = True

    while flag:
        error = None

        print(f"\n{current_path}    ₍^. .^₎⟆")
        input_data = input("$ ")
        setup_loggers()

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

            if True:
                # try:
                if command == "ls":
                    ls(current_path, command_data)

                    log("i", input_data)

                elif command == "cd":
                    if command_data is None:
                        error = "not enough arguments for cd"
                        log("e", error)
                        
                        with open("shell.log", "r") as f:
                            print(f.readlines()[-1].strip())

                    elif len(command_data) > 1:
                        error = "too many arguments for cd"
                        log("e", error)
                        
                        with open("shell.log", "r") as f:
                            print(f.readlines()[-1].strip())

                    else:
                        current_path = cd(current_path, command_data[0])

                        log("i", input_data)

                elif command == "cat":
                    if command_data is None:
                        cat(current_path, command_data)

                        log("i", input_data)

                    elif len(command_data) > 1:
                        error = "too many arguments for cat"
                        log("e", error)
                        
                        with open("shell.log", "r") as f:
                            print(f.readlines()[-1].strip())

                    else:
                        cat(current_path, command_data[0])

                        log("i", input_data)

                elif command == "cp":
                    if command_data is None:
                        error = "not enough arguments for cp"
                        log("e", error)
                        
                        with open("shell.log", "r") as f:
                            print(f.readlines()[-1].strip())

                    else:
                        cp(current_path, command_data)

                        log("i", input_data)
                        meta(input_data)

                elif command == "mv":
                    if command_data is None:
                        error = "not enough arguments for mv"
                        log("e", error)
                        
                        with open("shell.log", "r") as f:
                            print(f.readlines()[-1].strip())

                    else:
                        meta_data = mv(current_path, command_data)

                        log("i", input_data)
                        meta(meta_data)

                elif command == "rm":
                    if command_data is None:
                        error = "not enough arguments for rm"
                        log("e", error)
                        
                        with open("shell.log", "r") as f:
                            print(f.readlines()[-1].strip())

                    else:
                        rm(current_path, command_data)

                        log("i", input_data)

                elif command == "zip":
                    if command_data is None:
                        error = "not enough arguments for zip"
                        log("e", error)
                        
                        with open("shell.log", "r") as f:
                            print(f.readlines()[-1].strip())

                    elif len(command_data) != 2:
                        error = "wrong number of arguments for zip"
                        log("e", error)
                        
                        with open("shell.log", "r") as f:
                            print(f.readlines()[-1].strip())

                    else:
                        zip(current_path, command_data)

                        log("i", input_data)

                elif command == "unzip":
                    if command_data is None:
                        error = "not enough arguments for unzip"
                        log("e", error)
                        
                        with open("shell.log", "r") as f:
                            print(f.readlines()[-1].strip())

                    elif len(command_data) != 1:
                        error = "wrong number of arguments for unzip"
                        log("e", error)
                        
                        with open("shell.log", "r") as f:
                            print(f.readlines()[-1].strip())

                    else:
                        unzip(current_path, command_data)

                        log("i", input_data)

                elif command == "tar":
                    if command_data is None:
                        error = "not enough arguments for tar"
                        log("e", error)
                        
                        with open("shell.log", "r") as f:
                            print(f.readlines()[-1].strip())

                    elif len(command_data) != 2:
                        error = "wrong number of arguments for tar"
                        log("e", error)
                        
                        with open("shell.log", "r") as f:
                            print(f.readlines()[-1].strip())

                    else:
                        tar(current_path, command_data)

                        log("i", input_data)

                elif command == "untar":
                    if command_data is None:
                        error = "not enough arguments for untar"
                        log("e", error)
                        with open("shell.log", "r") as f:
                            print(f.readlines()[-1].strip())

                    elif len(command_data) != 1:
                        error = "wrong number of arguments for untar"
                        log("e", error)
                        
                        with open("shell.log", "r") as f:
                            print(f.readlines()[-1].strip())

                    else:
                        untar(current_path, command_data)

                        log("i", input_data)

                elif command == "grep":
                    if command_data is None:
                        error = "not enough arguments for grep"
                        log("e", error)
                        
                        with open("shell.log", "r") as f:
                            print(f.readlines()[-1].strip())

                    elif len(command_data) < 1:
                        error = "wrong number of arguments for grep"
                        log("e", error)
                        
                        with open("shell.log", "r") as f:
                            print(f.readlines()[-1].strip())

                    else:
                        grep(current_path, command_data)

                        log("i", input_data)

                elif command == "history":
                    if command_data is None:
                        history(command_data)

                    elif len(command_data) > 1:
                        error = "wrong number of arguments for history"

                        log("e", error)

                        with open("shell.log", "r") as f:
                            print(f.readlines()[-1].strip())

                    else:
                        history(command_data[0])

                elif command == "undo":
                    undo(current_path)

                elif command == "q":
                    flag = False
                    print("\n ---PROGRAM CLOSED--- \n")

                    with open("shell.log", "w", encoding="utf-8"):
                        pass

                    with open("meta.log", "w", encoding="utf-8"):
                        pass

                else:
                    error = f"unknown command {input_data}"
                    log("e", error)
                    with open("shell.log", "r") as f:
                        print(f.readlines()[-1].strip())

                    

            # except Exception as error:
            #     log("e", str(error))
            #     with open("shell.log", "r") as f:
            #         print(f.readlines()[-1].strip())


if __name__ == "__main__":
    main()
