import json

all_profit = 0
count = 0
firm_dict = {}
with open('ex7.txt', encoding='UTF - 8') as fout:
    for line in fout:
        line = line.split()
        profit = int(line[2]) - int(line[3])
        if profit > 0:
            all_profit += profit
        else:
            pass
        count += 1
        unit_dict = {line[0]: profit}
        firm_dict.update(unit_dict)
    my_list = [firm_dict, {'Average profit': all_profit / count}]
    print(my_list)
"""
json
"""
with open('ex7.json', 'w', encoding='UTF - 8') as fin:
    fin.write(json.dumps(my_list))
