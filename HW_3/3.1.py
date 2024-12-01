# Здесь решается по оператору **

user_num= float(input("Введите число, чтобы возвести его в степень: "))
degree = int(input("Введите степень числа: 0,1,2,3,4,5,6 или 7: "))

if 0 <= degree <=7:
    num_degree = user_num ** degree
    print(f"{user_num} в степени {degree} = ", num_degree)
else:
    print("Ошибка! Введите корректную степень числа")