d = {'1': "Один",
     '2': "Два",
     '3': "Три",
     '4': "Четыре"
     }

new_file = open('for_4(new)', 'w', encoding='utf-8')

with open('for_4.txt', 'r', encoding='utf-8') as f:
    a = f.readlines()
    for i in range(4):
        el = a[i].split()
        if el[2] in d:
            el[0] = d[el[2]]
        new_file.write(' '.join(el) + '\n')

new_file.close()
