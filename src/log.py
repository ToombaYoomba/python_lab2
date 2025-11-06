import logging

def setup_loggers():
    """
    Создание логин файлов для логирования

    Отдельно создаются логин файлы для комнад, доступных к откату
    И отдельно для всех команд и ошибок
    """
    # Логгер для meta.log
    
    meta_logger = logging.getLogger('meta')
    if not meta_logger.handlers:
        meta_logger.setLevel(logging.INFO)
        meta_handler = logging.FileHandler('meta.log', mode='a')
        meta_handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s %(message)s"))
        meta_logger.addHandler(meta_handler)
    
    # Логгер для shell.log
    shell_logger = logging.getLogger('shell')
    if not shell_logger.handlers:
        shell_logger.setLevel(logging.INFO)
        shell_handler = logging.FileHandler('shell.log', mode='a')
        shell_handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s %(message)s"))
        shell_logger.addHandler(shell_handler)

def meta(command, input_data):
    """
    Логирование команд с возможностью отката

    На вход получает команду и её данные
    """
    meta_logger = logging.getLogger('meta')
    meta_logger.info([command, input_data])

def log(flag, input_data):
    """
    Логирование команд и ошибок

    На вход получает команду и её данные, а также пометку для определения ошибки
    """
    shell_logger = logging.getLogger('shell')

    if flag == "e":
        shell_logger.error(input_data)
    else:
        shell_logger.info(input_data)

def hs(input_data):
    """
    Сохранение списка введённых пользователем команд

    На вход получает кввод пользователя в терминал
    """
    with open(".history", "a") as f:
        f.write(f"{input_data}\n")