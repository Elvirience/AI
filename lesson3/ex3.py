def num3(a, b, c, j):
    my_list = [a, b, c]
    """
    Определяю тип переменной: int или float
    """
    for i in my_list:
        if i.isdigit() is True:
            i = int(i)
        else:
            check = i.split('.')
            if len(check) == 2:
                if check[0].isdigit() and check[1].isdigit():
                    i = float(i)
        my_list[j] = i
        j += 1
    """
    Цикл на случай, если решение требует не использовать функцию ".sort()"
    """
    """
    j = 0
    while j < 2:
         if my_list[j] > my_list[j + 1]:
            my_list[j + 1] = my_list[j]
         else:
            j += 1
         j += 1
    """
    my_list.sort()
    print(my_list[1] + my_list[2])
    return my_list[1] + my_list[2]


a = input('a = ')
b = input('b = ')
c = input('c = ')
num3(a, b, c, 0)
