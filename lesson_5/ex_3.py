poor = []
sal = []
with open('for_3.txt', 'r', encoding='utf-8') as f:
    new = f.read().split('\n')
    for i in new:
        sal.append(int(i.split()[1]))
        if int(i.split()[1]) <= 20000:
            poor.append(i.split()[0])

print(sum(sal)//len(new))
print(poor)
