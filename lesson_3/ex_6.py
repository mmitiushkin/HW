def int_func(word):
    small = ord(word[0])
    big = chr(small - 32)
    return big + word[1:]


a = input(': ').split()
res = []
for word in a:
    res.append(int_func(word))
print(' '.join(res))
