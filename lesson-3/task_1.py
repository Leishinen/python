def divine(a, b):
    return a / b


a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
if b == 0:
    print("Ошибка! На ноль делить нельзя!")
else:
    print("Результат деления = ", divine(a, b))