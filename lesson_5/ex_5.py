with open('for_5.txt', 'w+', encoding='utf-8') as f:
    f.write(input(': '))

with open('for_5.txt', 'r', encoding='utf-8') as f:
    print(sum(map(int, f.readline().split())))
