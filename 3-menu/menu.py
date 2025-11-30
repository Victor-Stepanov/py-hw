category = input('Выберите желаемую категорию (напиток, суп, десерт): ')

if not category:
    category = input('Пожалуйста, выберите категорию: ')

match category:
    case 'напиток':
        user_input = input(
            'Укажите какой напиток из доступных (чай, кофе, сок): ')
        match user_input:
            case 'чай':
                print(f'Вы выбрали {user_input}, его стоимость 80 руб.')
            case 'кофе':
                print(f'Вы выбрали {user_input}, его стоимость 120 руб.')
            case 'сок':
                print(f'Вы выбрали {user_input}, его стоимость 100 руб.')
            case _:
                print('Такого напитка нет в меню')

    case 'суп':
        user_input = input(
            'Укажите какой суп из доступных (борщ, щи, суп-пюре): ')
        match user_input:
            case 'борщ':
                print(f'Вы выбрали {user_input}, его стоимость 350 руб.')
            case 'щи':
                print(f'Вы выбрали {user_input}, его стоимость 300 руб.')
            case 'суп-пюре':
                print(f'Вы выбрали {user_input}, его стоимость 280 руб.')
            case _:
                print('Такого супа нет в меню')

    case 'десерт':
        user_input = input(
            'Укажите какой десерт из доступных (торт, мороженое, фрукты): ')
        match user_input:
            case 'торт':
                print(f'Вы выбрали {user_input}, его стоимость 250 руб.')
            case 'мороженое':
                print(f'Вы выбрали {user_input}, его стоимость 150 руб.')
            case 'фрукты':
                print(f'Вы выбрали {user_input}, его стоимость 200 руб.')
            case _:
                print('Такого десерта нет в меню')

    case _:
        print('Такой категории нет в меню')
