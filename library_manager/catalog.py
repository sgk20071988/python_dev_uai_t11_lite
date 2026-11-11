"""Модуль управления каталогом книг библиотеки."""

from typing import Dict, List, Optional

from .utils.data_validation import validate_book_data


class Library:
    """Класс для управления коллекцией книг в библиотеке."""

    def __init__(self) -> None:
        # Внутреннее хранилище: список словарей с ключами title/author/genre
        self._books: list[dict[str, str]] = []

    def add_book(self, title: str, author: str, genre: str) -> bool:
        """Добавляет книгу в библиотеку.

        :return: True, если книга добавлена, False — если данные некорректны.
        """
        book_data = {"title": title, "author": author, "genre": genre}
        if not validate_book_data(book_data):
            return False

        # Проверка на дубликат по названию
        if any(book["title"].lower() == title.lower() for book in self._books):
            return False

        self._books.append(book_data)
        return True

    def remove_book(self, title: str) -> bool:
        """Удаляет книгу по названию.

        :return: True, если книга удалена, иначе False.
        """
        for index, book in enumerate(self._books):
            if book["title"].lower() == title.lower():
                del self._books[index]
                return True
        return False

    def find_by_title(self, title: str) -> Optional[Dict[str, str]]:
        """Ищет книгу по точному названию (без учёта регистра)."""
        for book in self._books:
            if book["title"].lower() == title.lower():
                return dict(book)
        return None

    def find_by_author(self, author: str) -> List[Dict[str, str]]:
        """Возвращает все книги указанного автора (без учёта регистра)."""
        return [
            dict(book)
            for book in self._books
            if book["author"].lower() == author.lower()
        ]

    def find_by_genre(self, genre: str) -> List[Dict[str, str]]:
        """Возвращает все книги указанного жанра (без учёта регистра)."""
        return [
            dict(book)
            for book in self._books
            if book["genre"].lower() == genre.lower()
        ]

    def get_all_books(self) -> List[Dict[str, str]]:
        """Возвращает копию списка всех книг в библиотеке."""
        return [dict(book) for book in self._books]

    def __len__(self) -> int:
        return len(self._books)

    def __repr__(self) -> str:
        return f"Library(books={len(self._books)})"