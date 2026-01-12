import sys

books = {
    "Преступление и наказание": "Фёдор Достоевский",
    "Война и мир": "Лев Толстой",
    "Мастер и Маргарита": "Михаил Булгаков",
    "1984": "Джордж Оруэлл",
    "Гордость и предубеждение": "Джейн Остин",
    "Сто лет одиночества": "Габриэль Гарсиа Маркес",
    "Улисс": "Джеймс Джойс",
    "Бесы": "Фёдор Достоевский",
    "Анна Каренина": "Лев Толстой",
    "Скотный двор": "Джордж Оруэлл",
    "Разум и чувства": "Джейн Остин",
    "Идиот": "Фёдор Достоевский",
    "Собачье сердце": "Михаил Булгаков",
    "Повелитель мух": "Уильям Голдинг",
    "Лолита": "Владимир Набоков"
}


# Базовый класс ошибки
class BooksError(Exception):
    """Базовый класс для ошибок"""
    pass


class UnknownCommandError(BooksError):
    """Ошибка: передана неизвестная команда"""
    pass


class CommandLineError(BooksError):
    """Ошибка: правильно запускается файл"""
    pass


class InvalidSortParameterError(BooksError):
    """Ошибка: передан некорректный параметр сортировки"""
    pass


class NoFilterTextError(BooksError):
    """Ошибка: не передан текст фильтра"""
    pass


def mapped(data: dict[str, str]):
    """Подготавливает результат в формате Книга — Автор"""
    return list(map(lambda title, author: f"{title} — {author}",
                    data.keys(), data.values()))


def sort_by_value(data: dict[str, str], value: str):
    """Логика для команды sort"""
    if value not in ["author", "book"]:
        raise InvalidSortParameterError(
            "Ошибка: сортировать можно только по author/book"
            "Пример: python main.py sort author"
        )

    sorted_index = 1 if value == "author" else 0
    return sorted(mapped(data), key=lambda x: x.split(" — ")[sorted_index])


def filter_by_value(data: dict[str, str], value: str):
    """Логика для команды filter"""
    if not value or not value.strip():
        raise NoFilterTextError(
            "Ошибка: текст для фильтрации не может быть пустым\n"
            "Пример: python main.py filter Толстой"
        )

    filtered_books = dict(filter(lambda item: value.lower()
                          in item[1].lower(), data.items()))
    return mapped(filtered_books)


def main():
    """Основная функция"""
    try:
        args = sys.argv[1:]

        if len(args) < 2:
            raise CommandLineError(
                "Использование: python main.py <action> <value>\n"
                "Пример: python main.py filter Толстой\n"
                "Пример: python main.py sort author"
            )

        action, value = args[0], args[1]

        commands = {
            "sort": sort_by_value,
            "filter": filter_by_value
        }

        if action not in commands:

            available_commands = ", ".join(commands.keys())

            raise UnknownCommandError(
                f"Ошибка: неизвестная команда '{action}'\n"
                f"Доступные команды: {available_commands}\n"
                "Пример: python main.py sort author"
            )

        result = commands[action](books, value)

        if result:
            for item in result:
                print(item)
        else:
            print("Ничего не найдено")

    except BooksError as e:
        print(f"[ERROR]: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"[UNEXPECTED ERROR]: {e}")
        sys.exit(2)


if __name__ == "__main__":
    main()
