import random

my_list = [random.randint(0, 20) for el in range(45)]
my_set = {el for el in my_list}
counts = {el: my_list.count(el) for el in my_set}
new_list = [el for el in my_list if counts.get(el) == 1]
print(my_list)
print(counts)
print(new_list)