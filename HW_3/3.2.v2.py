#Сначала я решила задачу, соорудив небоскреб из множественного ветвления. Оно
# даже работало, но было слишком длинным. Потом я подумала о сокращении
#и решила, что больше всего проблем из-за повторения формулы
#call_cost = call_time * стоимость оператора. Надо было откуда-то вытягивать стоимость.
#Словарь записался быстро, сложности были именно с извлечением значений - никак не могла понять,
# как писать another_operator. Но в итоге получилось!

call_time=abs(int(input("Введите время разговора:  ")))
user_operator = input("Выберите Вашего оператора: МТС, Билайн, Мегафон ")
another_operator = input("Выберите оператора, для совершения звонка: МТС, Билайн, Мегафон ")
dict1 = {'МТС':50,'Билайн':100, "Мегафон":150}
dict2 = {'МТС':90,'Билайн':60, "Мегафон":140}
dict3 = {'МТС':180,'Билайн':200, "Мегафон":30}
call_cost=0


if user_operator == "МТС":
    if another_operator  in dict1:
        call_cost = call_time * dict1.get(another_operator)
elif user_operator == "Билайн":
    if another_operator in dict2:
        call_cost = call_time * dict2.get(another_operator)
elif user_operator == "Мегафон":
    if another_operator  in dict3:
        call_cost = call_time * dict3.get(another_operator)
print(f"Стоимость звонка составит:  {call_cost} руб")