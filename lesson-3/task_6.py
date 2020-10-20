def int_func(s):
    return s.capitalize()


s = input("Введите слова латинскими буквами разделяя слова пробелами")
for word in s.split(' '):
    print(int_func(word), end=" ")
