"""
Вспомогательная функция к заданию "6", обрататывающая, по заданию, одно слово
"""


def helper(my_string, i):
    alphabet = (('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E'),
                ('f', 'F'), ('g', 'G'), ('h', 'H'), ('i', 'I'), ('j', 'J'),
                ('k', 'K'), ('l', 'L'), ('m', 'M'), ('n', 'N'), ('o', 'O'),
                ('p', 'P'), ('q', 'Q'), ('r', 'R'), ('s', 'S'), ('t', 'T'),
                ('u', 'U'), ('v', 'V'), ('w', 'W'), ('x', 'X'), ('y', 'Y'), ('z', 'Z'))
    while my_string[0] != alphabet[i][0]:
        i += 1
    print(alphabet[i][1] + my_string[1:])
    return alphabet[i][1] + my_string[1:]


"""
Здание 6.2. Например, вы ввели: aleksandra shapovalova
                   Результат: Aleksandra
                              Shapovalova
                              Aleksandra Shapovalova
        Первые две строки отображаются в результате работы функции "helper"
"""


def num6(string):
    """
    Список, чтобы собрать функцкцией .join()
    """
    my_list = []
    """
    Работа функции "helper" над каждым словом строки, введенной пользователем
    """
    for j in string.split(' '):
        my_list.append(helper(j, 0))
    """
    Сброка получившегося списка в строку
    """
    print(' '.join(my_list))
    return ' '.join(my_list)


q = ' '
while q != '':
    q = input('Введите номер задания или нажмите ENTER: ')
    if q == '6.1':
        my_string = input('Введите слово из маленьких латинских букв: ')
        helper(my_string, 0)
    elif q == '6.2':
        string = input('Введите слова из маленьких латинских букв: ')
        num6(string)