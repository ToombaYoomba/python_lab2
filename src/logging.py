from datetime import datetime


def logging(input_data):
    log_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log = log_time + " " + input_data

    with open("src/shell.log", "a", encoding="utf-8") as file:
        file.write(log + "\n")
