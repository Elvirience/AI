def num5(string, sum, j):
    """
    Суммирование вводимых чисел до того, как попадется специальный символ "q"
    """
    while string.count('q') == 0:
        my_list = string.split(' ')
        for i in my_list:
            sum += int(i)
        print(sum)
        string = input('Введите числа через пробел: ')
        string.count('q')
    """
    Как только строка содержит специальный символ, происходит суммирование чисел перед ним - работа завершается
    """
    my_list = string.split(' ')
    while my_list[j] != 'q':
        sum += int(my_list[j])
        j += 1
    print(sum)


string = input('Введите числа через пробел: ')
num5(string, 0, 0)
