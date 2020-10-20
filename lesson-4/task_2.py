import random

my_list = [random.randint(0, 100) for el in range(20)]
new_list = []
prev_el = my_list[0]
for el in my_list[1:]:
    if el > prev_el:
        new_list.append(el)
    prev_el = el
print(my_list)
print(new_list)

