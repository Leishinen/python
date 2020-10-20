def split_and_sum(str):
    n = 0
    sum = 0
    for c in str:
        if c == ' ':
            sum = sum + n
            n = 0
        elif c == '@':
            sum = sum + n
            return sum
        else:
            n = n * 10 + int(c)
    if n > 0:
        sum = sum + n
    return sum


do_interrupt = False
sum = 0
while not do_interrupt:
    str = input("Введите числа через пробел")
    if str != "@":
        sum = sum + split_and_sum(str)
        print(sum)
        if str.find('@') > -1:
            do_interrupt = True
    else:
        do_interrupt = True
