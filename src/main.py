from os import getcwd

from src.cat import cat
from src.cd import cd
from src.cp import cp
from src.logging import logging
from src.ls import ls
from src.mv import mv
from src.rm import rm
from src.zip import zip
from src.unzip import unzip
from src.tar import tar
from src.untar import untar
from src.grep import grep
from src.history import history


def main() -> None:
    current_path = getcwd().replace("\\", "/")
    # print(f"current path: {current_path}")

    flag = True

    while flag:
        error = None

        print(f"\n{current_path}    ₍^. .^₎⟆")
        input_data = input("$ ")

        if len(input_data) == 0 or len(input_data.strip()) == 0:
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

                    logging(input_data)

                elif command == "cd":
                    if command_data is None:
                        error = "ERROR: not enough arguments for cd"
                        print(error)

                        logging(error)

                    elif len(command_data) > 1:
                        error = "ERROR: too many arguments for cd"
                        print(error)

                        logging(error)

                    else:
                        current_path = cd(current_path, command_data[0])

                        logging(input_data)

                elif command == "cat":
                    if command_data is None:
                        cat(current_path, command_data)

                        logging(input_data)

                    elif len(command_data) > 1:
                        error = "ERROR: too many arguments for cat"
                        print(error)

                        logging(error)

                    else:
                        cat(current_path, command_data[0])

                        logging(input_data)

                elif command == "cp":
                    if command_data is None:
                        error = "ERROR: not enough arguments for cp"
                        print(error)

                        logging(error)

                    else:
                        cp(current_path, command_data)

                        logging(input_data)

                elif command == "mv":
                    if command_data is None:
                        error = "ERROR: not enough arguments for mv"
                        print(error)

                        logging(error)

                    else:
                        mv(current_path, command_data)

                        logging(input_data)

                elif command == "rm":
                    if command_data is None:
                        error = "ERROR: not enough arguments for rm"
                        print(error)

                        logging(error)

                    else:
                        rm(current_path, command_data)

                        logging(input_data)

                elif command == "zip":
                    if command_data is None:
                        error = "ERROR: not enough arguments for zip"
                        print(error)

                        logging(error)
                    
                    elif len(command_data) != 2:
                        error = "ERROR: wrong number of arguments for zip"
                        print(error)

                        logging(error)

                    else:
                        zip(current_path, command_data)

                        logging(input_data)

                elif command == "unzip":
                    if command_data is None:
                        error = "ERROR: not enough arguments for unzip"
                        print(error)

                        logging(error)
                    
                    elif len(command_data) != 1:
                        error = "ERROR: wrong number of arguments for unzip"
                        print(error)

                        logging(error)

                    else:
                        unzip(current_path, command_data)

                        logging(input_data)

                elif command == "tar":
                    if command_data is None:
                        error = "ERROR: not enough arguments for tar"
                        print(error)

                        logging(error)
                    
                    elif len(command_data) != 2:
                        error = "ERROR: wrong number of arguments for tar"
                        print(error)

                        logging(error)

                    else:
                        tar(current_path, command_data)

                        logging(input_data)

                elif command == "untar":
                    if command_data is None:
                        error = "ERROR: not enough arguments for untar"
                        print(error)

                        logging(error)
                    
                    elif len(command_data) != 1:
                        error = "ERROR: wrong number of arguments for untar"
                        print(error)

                        logging(error)

                    else:
                        untar(current_path, command_data)

                        logging(input_data)

                elif command == "grep":
                    if command_data is None:
                        error = "ERROR: not enough arguments for grep"
                        print(error)

                        logging(error)
                    
                    elif len(command_data) < 1:
                        error = "ERROR: wrong number of arguments for grep"
                        print(error)

                        logging(error)

                    else:
                        grep(current_path, command_data)

                        logging(input_data)

                elif command == "history":
                    if command_data is None:
                        history(command_data)
                        
                    elif len(command_data) > 1:
                        error = "ERROR: wrong number of arguments for history"
                        print(error)

                        logging(error)

                    else:

                        history(command_data[0])

                elif command == "q":
                    flag = False
                    print("\n ---PROGRAM CLOSED--- \n")

                    with open("src/shell.log", "w", encoding="utf-8"):
                        pass

                else:
                    error = f"ERROR: unknown command {input_data}"
                    print(error)

                    logging(error)

            # except Exception as error:
            #     print(f"Error: {error}")

            #     logging("Error: " + str(error))


if __name__ == "__main__":
    main()
