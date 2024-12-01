sales_1= int(input("Введите уровень продаж для менеджера Васи: "))
sales_2 = int(input("Введите уровень продаж для менеджера Пети: "))
sales_3 = int(input("Введите уровень продаж для менеджера Маши: "))
salary_1 = 0
salary_2 = 0
salary_3 = 0


if sales_1 <= 500:
    salary_1 = 200 + sales_1*0.03
elif 500 < sales_1 <= 1000:
    salary_1 = 200 + sales_1*0.05
elif 1000 < sales_1:
    salary_1 = 200 + sales_1*0.08

if sales_2 <= 500:
    salary_2 = 200 + sales_2*0.03
elif 500 < sales_2 <= 1000:
    salary_2 = 200 + sales_2*0.05
elif 1000 < sales_2:
    salary_2 = 200 + sales_2*0.08

if sales_3 <= 500:
    salary_3 = 200 + sales_3*0.03
elif 500 < sales_3 <= 1000:
    salary_3 = 200 + sales_3*0.05
elif 1000 < sales_3:
    salary_3 = 200 + sales_3*0.08

if salary_2 < salary_1 and salary_1 > salary_3:
    print("Лучший по продажам - Менеджер Вася!")
    print ("С учетом премии мы выплатим  ", salary_1+200, "долларов!")
elif salary_1 < salary_2 and salary_2>salary_3:
    print("Лучший по продажам - Менеджер Петя!")
    print ("С учетом премии мы выплатим  ", salary_2+200, "долларов!")
elif salary_2 < salary_3 and salary_3 > salary_1:
    print("Лучший по продажам - Менеджер Маша!")
    print ("С учетом премии мы выплатим  ", salary_3+200, "долларов!")
else:
    if salary_1==salary_2==salary_3:
        print("Победила дружба, премию поделите на троих")