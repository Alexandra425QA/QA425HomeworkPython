month = 1
money = 0
for i in range(1, 13, 1):
    result = float(input("Введите сумму, отложенную в копилку в месяц {}:".format(month)))
    money += result
    month += 1
print("Общая сумма накопления:", money)10