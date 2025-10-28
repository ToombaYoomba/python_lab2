def history(N = None):

    if N is None:
        with open("src/shell.log", "r") as f:
            for line in f.readlines():
                print(line.strip())

    else:
        try:
            N = int(N)
        except Exception:
            print("wrong argument for history")
        with open("src/shell.log", "r") as f:
                
                lines = f.readlines()
                for i in range(N):
                    try:
                        print(lines[i].strip())

                    except Exception:
                        return 0