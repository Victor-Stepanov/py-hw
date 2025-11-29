food, transport, entertainment = map(float, input(
    "Укажите цену за еду, транспорт, развлечение: ").split())

result = food + transport + entertainment
average = result / 3
print(
    f'Итоговая сумма потраченных средств: {result}')
print(f'Среднее значение: {average}')
