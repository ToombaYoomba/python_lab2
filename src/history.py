def history(N = None):
    """
    Вывод последних № введённых команд с ихномерами

    На вход получает число команд для вывода
    Команды берёт из shell.log
    Выводит ошибки пользователя
    Если нету аргумента числа - выводит все команды из истории
    """

    if N is None:
        with open("src/shell.log", "r") as f:
            for line in f.readlines():
                print(line.strip())

    else:
        try:
            N = int(N)
        except Exception:
            print("wrong argument for history")
        with open("shell.log", "r") as f:
                
                lines = f.readlines()
                i = -N
                while i < 0:
                    try:
                        print(lines[i].strip())
                        i += 1

                    except Exception:
                        return 0