from itertools import cycle, count


def my_func1(x, y):
    for i in count(x):
        print(i)
        if i == y:
            break


def my_func2(my_list, iteration):
    i = 0
    el = cycle(my_list)
    while i < iteration:
        print(next(el))
        i += 1


my_func1(3, 10)
my_func2([1, 2, 3], 10)
