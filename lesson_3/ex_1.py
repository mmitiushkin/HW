def my_func(x, y):
    if y == 0:
        return 'Ошибка'
    return round(x / y, 2)


print(my_func(int(input(': ')), int(input(': '))))
