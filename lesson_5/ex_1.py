a = " "
with open('for_1.txt', 'w') as f:
    while bool(a):
        a = input(': ')
        f.write(a + '\n')
