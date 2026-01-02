MENU_ITEMS = ["Добавить расход", "Показать все расходы",
              "Показать сумму и средний расход", "Удалить расход по номеру",
              "Выход"]

ERROR_MESSAGE = 'Выбранный пункт меню находится в разработке'
ERROR_UNKNOWN_COMMAND = 'Указанная команда отсутствует в списке доступных'


print('Доступные команды в меню:')
for item in MENU_ITEMS:
    print(item, end='\n')

while True:
    choice = input("Укажите команду из доступных:").lower()

    match choice:
        case 'выход':
            break
        case 'добавить расход':
            print(ERROR_MESSAGE)
        case 'показать все расходы':
            print(ERROR_MESSAGE)
        case 'показать сумму и средний расход':
            print(ERROR_MESSAGE)
        case 'удалить расход по номеру':
            print(ERROR_MESSAGE)
        case _:
            print(ERROR_UNKNOWN_COMMAND)
