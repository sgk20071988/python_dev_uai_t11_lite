"""Модуль генерации отчётов о книгах."""

from .catalog import Library
from .utils.formatting import format_book_data


def generate_report(library: Library) -> str:
    """Генерирует текстовый отчёт о всех книгах в библиотеке.

    :param library: объект Library.
    :return: многострочная строка с перечнем книг.
    """
    books = library.get_all_books()

    if not books:
        return "Library is empty."

    lines = [f"Library report ({len(books)} book(s)):"]
    for index, book in enumerate(books, start=1):
        lines.append(f"{index}. {format_book_data(book)}")

    return "\n".join(lines)