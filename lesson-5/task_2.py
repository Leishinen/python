file = open(r"C:\Users\Leishinen\Desktop\Курсы\PyProjects\file1.txt", "r")

lines = 0
words = 0

for line in file:
    words_in_line = len(line.split(" "))
    print("Количество слов в строке = ", words_in_line)
    lines = lines + 1

print("Количество строк = ", lines)
file.close()
