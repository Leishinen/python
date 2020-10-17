import random
file = open(r"C:\Users\Leishinen\Desktop\Курсы\PyProjects\file5.txt", "w")

list = [random.randint(0, 100) for el in range(20)]
for num in list:
    file.write(str(num) + " ")
file.close()

file = open(r"C:\Users\Leishinen\Desktop\Курсы\PyProjects\file5.txt", "r")

content = file.readline()
numbers = content.split(" ")
sum = 0
for number in numbers:
    if number:
        sum = sum + int(number)
print(sum)
file.close()