"""Генератор приветствий."""


def greeting(name: str) -> str:
    """Возвращает текст приветствия.

    Args:
        name: Имя пользователя

    Returns:
        str: Текст приветствия
    """
    cor_name = str(name.title())
    return "Привет, %s" % cor_name  # noqa: WPS323, Q000
