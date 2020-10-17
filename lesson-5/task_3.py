file = open(r"C:\Users\Leishinen\Desktop\Курсы\PyProjects\file2.txt", "r", encoding="utf-8")

sum = 0
count = 0
for line in file:
    employee_data = line.split(" ")

    family = employee_data[0]
    salary = int(employee_data[1])

    if salary < 20000:
        print(family)
    count = count + 1
    sum = sum + salary
avg = sum / count
print(avg)
file.close()
