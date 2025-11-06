def history(N = None):
    """
    Вывод последних № введённых команд с ихномерами

    На вход получает число команд для вывода
    Команды берёт из shell.log
    Выводит ошибки пользователя
    Если нету аргумента числа - выводит все команды из истории
    """

    result = []

    if N is None:
        with open("shell.log", "r") as f:
            for line in f.readlines():
                result.append(line.strip().split(" ", maxsplit=2)[2])
                # print(line.strip().split(" ", maxsplit=2)[2])

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
                        result.append(lines[i].strip().split(" ", maxsplit=2)[2])
                        # print(lines[i].strip().split(" ", maxsplit=2)[2])
                        i += 1

                    except Exception:
                        return 0
                    
    return result