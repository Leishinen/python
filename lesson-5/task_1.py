file = open("file.txt", "x")
while True:
    text = input()
    file.write(text + "\n")
    if text == "":
        break
file.close()
