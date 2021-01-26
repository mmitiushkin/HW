b = (input(': '))
a = []

while b != 'q':
    b = b.split()
    for i in b:
        a.append(int(i))
    print(sum(a))
    b = (input(': '))
