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


def mapped(data: dict[str, str]):
    """ Подготавливает результат в формате Книга — Автор """
    return list(map(lambda title, author: f"{title} — {author}",
                    data.keys(), data.values()))


def sort_by_value(data: dict[str, str], value: str):
    """Логика для команды sort"""
    if value not in ["author", "book"]:
        print("Ошибка: сортировать можно только по author/book")
        sys.exit(1)

    sorted_index = 1 if value == "author" else 0

    return sorted(mapped(data),
                  key=lambda x: x.split(" — ")[sorted_index])


def filter_by_value(data: dict[str, str], value: str):
    """Логика для команды filter"""
    filtered_books = dict(filter(lambda item: value.lower()
                          in item[1].lower(), data.items()))

    return mapped(filtered_books)


def main():
    """Основная ф-ция"""
    args = sys.argv[1:]

    if len(args) < 2:
        print("Использование: python main.py <action> <value>")
        print("Пример: python main.py filter Толстой")
        print("Пример: python main.py sort author")
        sys.exit(1)
    action, value = args

    commands = {
        "sort": sort_by_value,
        "filter": filter_by_value
    }

    if action not in commands:
        print(f"Ошибка: неизвестная команда {action}")
        print(f"Доступные команды: {", ".join(commands.keys())}")
        sys.exit(1)

    result = commands[action](books, value)

    if result:
        for item in result:
            print(item)
    else:
        print("Ничего не найдено")


if __name__ == "__main__":
    main()
