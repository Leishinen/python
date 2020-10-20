from sys import argv

script_name, output_in_hours, rate_per_hour, bonus = argv

salary = (float(output_in_hours) * float(rate_per_hour)) + float(bonus)
print("зарплата = ", salary)