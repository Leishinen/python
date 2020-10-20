from functools import reduce

def my_func (prev_el, el):
    return prev_el * el
my_list = reduce(my_func, [el for el in range (100, 1001) if el % 2 == 0])
print(my_list)
