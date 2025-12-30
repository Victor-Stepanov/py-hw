user_input = list(map(float, input().split()))


if len(user_input) != 7:
    print("Нужно ввести ровно 7 чисел")
else:

    min_value = min(user_input)
    max_value = max(user_input)
    total_sum = sum(user_input)
    average = total_sum / 7

    print(f"Сумма: {total_sum}")
    print(f"Среднее: {average}")
    print(f"Минимум: {min_value}")
    print(f"Максимум: {max_value}")

    result = (min_value, max_value, total_sum)
    print(result)
