def my_func(a, b, c):
    d = 0
    if a + b > d:
        d = a + b
    if a + c > d:
        d = a + c
    if b + c > d:
        d = b + c
    return d


a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
c = int(input("Введите третье число"))

d = my_func(a, b, c)
print(d)


