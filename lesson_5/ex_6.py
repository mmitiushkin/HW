subj = {}
with open('for_6.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        new_line = line.replace('(', ' ').split()
        subj[new_line[0][:-1]] = sum(int(i) for i in new_line if i.isdigit())
print(subj)
