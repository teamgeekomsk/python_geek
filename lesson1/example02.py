time = int(input("Введите время в секундах "))
hour = ((time // 3600)) % 24
minute = (time // 60) % 60
second = time % 60
if minute < 10:
    minute = str('0' + str(minute))
else:
    minute = str(minute)
if second < 10:
    second = str('0' + str(second))
else:
    second = str(second)
print(str(hour) + ':' + str(minute) + ':' + str(second))
