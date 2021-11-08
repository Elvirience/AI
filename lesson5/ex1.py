fin = open('ex1.txt', 'w', encoding='UTF-8')
data = input('Введите данные для записи в файл или пустую строку: ')
while data != '':
    fin.write(data + '\n')
    data = input('Введите данные для записи в файл или пустую строку: ')
fin.close()
