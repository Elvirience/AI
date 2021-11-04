from itertools import count, cycle

a = int(input('Стартовое число: '))
b = int(input('Шаг: '))
c = int(input('Предел: '))


def num6_1(a, b, c):
    for i in count(a, b):
        if i >= c:
            break
        yield i


for el in num6_1(a, b, c):
    print(el)
