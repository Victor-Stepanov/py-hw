user_input = input()

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

result = rub + kop / 100
print(f"{result:.2f} ₽")
