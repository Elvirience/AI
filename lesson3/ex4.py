def num4(x, y):
    for i in range(abs(y)):
        x *= x
    print(1 / x)
    return 1 / x


x = abs(float(input('Введите действительное положительное число: ')))
y = int(input('Введите целое отрицательное число: '))
num4(x, y)
