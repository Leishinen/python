from sys import argv
from itertools import cycle
import random

number = argv[1]
my_list = [random.randint(0, 150) for el in range(10)]

c = 0
for el in cycle(my_list):
    if c > int(number):
        break
    print(el)
    c += 1
print(number)

