def num1(a, b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('Деление на 0')
        print('Попробуте еще раз!')
        a = int(input('Числитель = '))
        b = int(input('Знаменатель = '))
        print(a / b)
    return a/b


a = int(input('Числитель = '))
b = int(input('Знаменатель = '))
num1(a, b)
