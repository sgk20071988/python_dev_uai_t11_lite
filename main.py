from library_manager import Library, generate_report


def main() -> None:
    library = Library()

    library.add_book("Война и мир", "Лев Толстой", "Роман")
    library.add_book("Преступление и наказание", "Фёдор Достоевский", "Роман")
    library.add_book("Мастер и Маргарита", "Михаил Булгаков", "Мистика")

    print(generate_report(library))
    print()

    print("Поиск по автору 'Лев Толстой':", library.find_by_author("Лев Толстой"))
    print("Поиск по жанру 'Роман':", library.find_by_genre("Роман"))
    print("Поиск по названию 'Мастер и Маргарита':",
          library.find_by_title("Мастер и Маргарита"))

    library.remove_book("Война и мир")
    print("\nПосле удаления 'Война и мир':")
    print(generate_report(library))


if __name__ == "__main__":
    main()