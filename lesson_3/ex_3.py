def my_func(x, y, z):
    a = [x, y, z]
    b = []
    for i in range(2):
        b.append(max(a))
        a.remove(max(a))
    return sum(b)


print(my_func(1, 3, 5))
