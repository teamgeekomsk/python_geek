num = int(input("Введите число больше 10 "))
ls = []
while num > 10:
    ls.append(num % 10)
    num //= 10
result = max(ls)
print(result)
