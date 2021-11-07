import json

with open('data7.json', 'w', encoding='utf-8') as file_j:
    with open('data7.txt', 'r', encoding='utf-8') as file:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in file}
        my_data = [profit, {'average_profit': round(
            sum([el for el in profit.values() if el > 0]) / len([i for i in profit.values() if i > 0]))}]
    json.dump(my_data, file_j)
