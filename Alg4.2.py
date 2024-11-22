month = 1
money = 0
while month <= 12:
    result = float(input("Введите сумму, отложенную в копилку в месяц {}:".format(month)))
    money += result
    month += 1
print("Общая сумма накопления:", money)