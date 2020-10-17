file = open(r"C:\Users\Leishinen\Desktop\Курсы\PyProjects\file6.txt", "r", encoding="utf-8")

disciplines_dict = {}

for line in file:
    discipline_data = line.split(" ")

    count = 0
    discipline = discipline_data[0].replace(":", "")
    for course_data in discipline_data[1:]:
        hours_str = course_data.replace("(л)", "").replace("(лаб)", "").replace("(пр)", "")
        if hours_str and hours_str != "—":
            count = count + int(hours_str)
    disciplines_dict[discipline] = count
file.close()

print(disciplines_dict)
