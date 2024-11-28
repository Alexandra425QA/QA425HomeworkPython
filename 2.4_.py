#попытка решения через диапазон
num= int(input("Пожалуйста, введите число в диапазоне от 1 до 100: "))
range_nums = range(1, 100)

if num in range_nums:
    if num % 5 == 0 and num % 3 == 0:
        print("Fizz Buzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
else:
    print("Ошибка! Введите значение из указанного диапазона")