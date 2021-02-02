# Задание 3
"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""
# Начало программы
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
month = int(input("Введите месяц по номеру "))
if month in (12, 1, 2):
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif month in (3, 4, 5):
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month in (6, 7, 8):
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif month in (9, 10, 11):
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
    print("Error 404")
