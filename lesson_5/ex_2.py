with open('for_2.txt', 'r') as f:
    a = f.readlines()
    print(f'Всего {len(a)} строки \n')
    for i in range(len(a)):
        print(f'В {i+1} строке - {len(a[i].split())} слова')
