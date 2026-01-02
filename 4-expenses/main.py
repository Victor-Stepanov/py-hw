# Utils
def print_all_expenses(expenses: list[tuple[str, str]]) -> None:
    '''
    Хелпер для отрисовки всего списка расходов
    '''
    for index, expense in enumerate(expenses):
        print(f"{index}. {expense[0]}: {expense[1]}₽")


def get_user_expense_value():
    '''
    Получает сумму расхода от пользователя и преобразует
    её в формат с плавающей точкой

    '''
    user_input = input("Укажите прайс:")

    parts = user_input.strip().lower().split()

    has_rub = "руб" in parts
    has_kop = "коп" in parts

    if not has_rub and not has_kop:
        print("Некорректный формат суммы")
        exit()

    rub, kop = 0, 0

    if has_rub:
        index_rub = parts.index("руб")
        if index_rub > 0:
            rub_str = parts[index_rub - 1]
            if rub_str.isdigit():
                rub = int(rub_str)

    if has_kop:
        index_kop = parts.index("коп")
        if index_kop > 0:
            kop_str = parts[index_kop - 1]
            if kop_str.isdigit():
                kop = int(kop_str)

    if kop >= 100:
        rub += kop // 100
        kop = kop % 100

    return str(rub + kop / 100)


def add_expense(expenses: list[tuple[str, str]], value: tuple[str, str]):
    '''
    Добавляет новый расход в список
    '''
    expenses.append(value)


def delete_expense(expenses: list[tuple[str, str]], index: int) -> None:
    '''
    Удаляет расход по указанному индексу
    '''
    if 0 <= index < len(expenses):
        expenses.pop(index)
    else:
        print(f"Ошибка: индекс {index} вне диапазона")


def get_total(expenses: list[tuple[str, str]]) -> float:
    '''
    Вычисляет общую сумму всех расходов
    '''
    total_sum = 0.0

    for expense in expenses:
        value = expense[1]
        if value.replace('.', '', 1).isdigit():
            total_sum += float(value)

    return total_sum


def get_average(expenses: list[tuple[str, str]]) -> float:
    '''
    Вычисляет средний расход
    '''
    if len(expenses) == 0:
        return 0.0
    return get_total(expenses) / len(expenses)


def print_report(expenses: list[tuple[str, str]]) -> None:
    '''
    Формирует и выводит полный отчет по расходам
    '''
    if not expenses:
        print("Нет данных о расходах")
        return

    print("\n" + "="*50)
    print("ОТЧЕТ ПО РАСХОДАМ".center(50))
    print("="*50)

    print("\nДетализированный список расходов:")
    print("-"*50)

    valid_expenses: list[tuple[str, float]] = []
    for i, (name, amount) in enumerate(expenses, 1):
        if amount.replace('.', '', 1).isdigit():
            amount_float = float(amount)
            print(f"{i:2}. {name:<30} {amount_float:>10.2f}₽")
            valid_expenses.append((name, amount_float))
        else:
            print(f"{i:2}. {name:<30} {'Некорр. сумма':>10}")

    print("-"*50)

    # Статистика
    total = get_total(expenses)
    average = get_average(expenses)

    print("\nСтатистика:")
    print(f"Количество расходов: {len(expenses)}")
    print(f"Общая сумма: {total:.2f}₽")
    print(f"Средний расход: {average:.2f}₽")

    if valid_expenses:
        max_expense = valid_expenses[0]
        for expense in valid_expenses:
            if expense[1] > max_expense[1]:
                max_expense = expense

        min_expense = valid_expenses[0]
        for expense in valid_expenses:
            if expense[1] < min_expense[1]:
                min_expense = expense

        print(
            f"Самый дорогой расход: {max_expense[0]} - {max_expense[1]:.2f}₽")
        print(
            f"Самый дешевый расход: {min_expense[0]} - {min_expense[1]:.2f}₽")
    elif expenses:
        print(
            "Не удалось определить самый дорогой/дешевый расход "
            "из-за некорректных данных")

    print("="*50 + "\n")


def show_menu() -> None:
    '''
    Отображает главное меню программы
    '''
    print("""
    УЧЕТ РАСХОДОВ
    -------------
    1. Добавить расход
    2. Удалить расход по его номеру
    3. Показать все расходы
    4. Показать средний расход
    5. Показать сумму расходов
    6. Сформировать полный отчет
    0. Выход
    -------------""")


ERROR_UNKNOWN_COMMAND = 'Указанная команда отсутствует в списке доступных'


def main():
    '''
    Главная функция программы, реализующая основной цикл работы
    '''
    show_menu()
    expenses = [('Хлеб-0', '100'), ('Хлеб-1', '100'),
                ('Хлеб-2', '100'), ('Хлеб-3', '100'), ('Хлеб-4', '100')]

    while True:
        choice = input("\nВыберите пункт меню: ").strip()

        match choice:
            case "0":
                print("Выход из программы. До свидания!")
                break
            case "1":
                name = input("Укажите название расхода: ").strip()
                if name:
                    amount = get_user_expense_value()
                    add_expense(expenses, (name, amount))
                    print(
                        f"Расход '{name}' на сумму {amount}₽ успешно добавлен")
                else:
                    print("Ошибка: название расхода не может быть пустым")
            case "2":
                if expenses:
                    print_all_expenses(expenses)
                    index_input = input("Укажите индекс удаляемого расхода: ")
                    if index_input.isdigit():
                        index = int(index_input)
                        delete_expense(expenses, index)
                        print("Расход успешно удален")
                    else:
                        print("Ошибка: индекс должен быть числом")
                else:
                    print("Список расходов пуст")
            case "3":
                if expenses:
                    print("\nСписок всех расходов:")
                    print_all_expenses(expenses)
                else:
                    print("Список расходов пуст")
            case "4":
                print(f"Средний расход: {get_average(expenses):.2f}₽")
            case "5":
                print(f"Сумма всех расходов: {get_total(expenses):.2f}₽")
            case "6":
                print_report(expenses)
            case _:
                print(ERROR_UNKNOWN_COMMAND)
                show_menu()


if __name__ == "__main__":
    main()
