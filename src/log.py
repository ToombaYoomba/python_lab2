import logging

def setup_loggers():
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

def meta(input_data):
    meta_logger = logging.getLogger('meta')
    meta_logger.info(input_data)

def log(flag, input_data):
    shell_logger = logging.getLogger('shell')

    if flag == "e":
        shell_logger.error(input_data)
    else:
        shell_logger.info(input_data)