water = int(input("Введите объем доставленной воды (л): "))

if 20000 <= water< 30000:
    bonus = "Бонус=10%"
elif 30000 <= water:
    bonus = "Бонус=20%"
else:
    bonus = "Премия не полагается"
print(bonus)