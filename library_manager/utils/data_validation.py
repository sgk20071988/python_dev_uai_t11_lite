"""Модуль валидации данных книг."""

from typing import Any

REQUIRED_FIELDS = ("title", "author", "genre")


def validate_book_data(data: dict) -> bool:
    """Проверяет корректность данных книги.

    Данные считаются корректными, если:
      * data является словарём;
      * содержит все обязательные поля: title, author, genre;
      * значения полей — непустые строки.

    :param data: словарь с данными книги.
    :return: True, если данные корректны, иначе False.
    """
    if not isinstance(data, dict):
        return False

    for field in REQUIRED_FIELDS:
        value: Any = data.get(field)
        if not isinstance(value, str) or not value.strip():
            return False

    return True