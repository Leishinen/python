from sys import argv
from itertools import count

number = argv[1]
for el in count(int(number)):
    if el > 100:
        break
    else:
        print(el)