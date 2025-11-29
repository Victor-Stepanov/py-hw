price = float(input('Укажите стоимость товара: '))
discount = int(input('Укажите процент скидки: '))

final_price = price - (price * (discount / 100))

print(f'Стоимость товара с учетом вашей скидки: {final_price}')
