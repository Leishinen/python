def my_func(x, y):
    b = 1
    for i in range(abs(y)):
        b = b * x
    return 1 / b


x = float(input("Введите действительное положительное число"))
y = int(input("Введите целое отрицательное число"))

print("Степень y числа x = ", my_func(x, y))
