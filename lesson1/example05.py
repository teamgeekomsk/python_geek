a = int(input("Введите значение выручки >>>"))
b = int(input("Введите значение издержек >>>"))
if a > b:
    print("Компания работает с прибылью")
    print("Соотношение выручки к издержкам составляет " + str(a / b))
    c = int(input("Введите количество сотрудников >>>"))
    print("Прибыль фирмы в расчете на одного сотрудника составляет " + str((a - b) / c))
else:
    print("Компания работает с убытками")
