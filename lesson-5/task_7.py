import json

profits = {}
profit_sum = 0
profits_count = 0
with open(r"C:\Users\Leishinen\Desktop\Курсы\PyProjects\file7.txt", "r", encoding="utf-8") as firms_file:
    for line in firms_file:
        data_list = line.split(" ")

        firm_name = data_list[0]
        revenue = int(data_list[2])
        cost = int(data_list[3])

        profit = revenue - cost
        if profit > 0:
            profit_sum = profit_sum + profit
            profits_count = profits_count + 1
        profits[firm_name] = profit

with open(r"C:\Users\Leishinen\Desktop\Курсы\PyProjects\file7_profits.txt", "w", encoding="utf-8") as profits_file:
    json.dump([profits, {"average_profit": profit_sum / profits_count}], profits_file)

