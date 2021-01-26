def my_func(x, y):
    global res
    for i in range(abs(y)-1):
        res = x * x
    return 1/res


print(my_func(10, -3))
