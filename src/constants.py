TRASH_PATH = "trash"

class FuncError(Exception):
    """Ошибки основных функций."""

    pass

class AddFuncError(Exception):
    """Ошибки вспомогательных функций."""

    pass

class MainError(Exception):
    """Ошибки ввода в main."""

    pass