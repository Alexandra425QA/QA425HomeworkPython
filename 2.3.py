print ("Добро пожаловать в конвертер мер длины!")
a= abs(float(input("Введите длину в метрах: "))) # чтобы не ввели отрицательное значение
vybor = input ("Выберите длину, в которую хотите перевести: 1 - мили, 2- дюймы, 3 -ярды: ")

if vybor=="1":
    miles = a * 0.000621
    print ("Длина в милях = ", miles)
elif vybor == "2":
    inches = a * 0.0254
    print("Длина в дюймах = ", inches)
elif vybor == "3":
    yards = a * 1.09
    print("Длина в ярдах = ", yards)
else:
     print("Ошибка выбора! Пожалуйста, введите корректное значение")