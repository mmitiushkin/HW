from json import dumps

res = [{}, {}]

with open('for_7.txt', encoding='utf-8') as fhs:
    lines = fhs.readlines()

for line in lines:
    name, _, proceeds, expenses = line.split()
    res[0][name] = int(proceeds) - int(expenses)

res[1]['average_profit'] = round(
    sum(profit for _, profit in res[0].items() if profit > 0) / len(res[0]))

with open('for_7(new).json', "w", encoding='utf-8') as fhd:
    fhd.write(dumps(res))
