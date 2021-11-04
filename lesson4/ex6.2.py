from itertools import count, cycle


def num6_2(my_list, steps, counter=0):
    for i in cycle(my_list):
        """
        steps*len(my_list) - число шагов в одном обороте "cycle()"
        """
        if counter >= steps*len(my_list):
            break
        yield i
        counter += 1


my_list = []
el = input('Введите элемент списка или ENTER: ')
while el != '':
    my_list.append(el)
    el = input('Введите элемент списка или ENTER: ')
print('Оборот - полное прохождение "cycle()" по аргументу-списку')
steps = int(input('Введите число оборотов "cycle()": '))
for el in num6_2(my_list, steps, 0):
    print(el)
