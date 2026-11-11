"""Модуль форматирования данных книг для отчётов."""


def format_book_data(data: dict) -> str:
    """Форматирует данные книги в строку для отчёта.

    Пример результата:
        Title: Война и мир, Author: Лев Толстой, Genre: Роман

    :param data: словарь с данными книги (title, author, genre).
    :return: отформатированная строка.
    """
    return (
        f"Title: {data.get('title', 'Unknown')}, "
        f"Author: {data.get('author', 'Unknown')}, "
        f"Genre: {data.get('genre', 'Unknown')}"
    )