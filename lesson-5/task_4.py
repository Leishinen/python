file = open(r"C:\Users\Leishinen\Desktop\Курсы\PyProjects\file3.txt", "r")
file2 = open(r"C:\Users\Leishinen\Desktop\Курсы\PyProjects\file4.txt", "w")

for line in file:
    str = line.replace("One", "Один")
    str = str.replace("Two", "Два")
    str = str.replace("Three", "Три")
    str = str.replace("Four", "Четыре")

    file2.write(str)
file.close()
file2.close()