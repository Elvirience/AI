result_dict = {}
with open('ex6.txt', encoding='UTF - 8') as fout:
    for line in fout:
        line = line.split()
        """
        Для каждой строки обнуляю общее число занятий по предмету
        """
        sum = 0
        for element in line:
            """
            Ищу символы в элементах списка строк, которые на самом деле являются числами
            Перед проверкой каждого элемента списка строка пустая
            """
            string = ''
            for symbol in element:
                try:
                    int(symbol)
                    string += symbol
                except ValueError:
                    pass
            """
            Обработка исключений на случай, 
             если стоит прочерк (чтобы не int(string), где string = '')
            В остальных случаях прибавляю найденное число занятий
            """
            try:
                sum += int(string)
            except ValueError:
                pass
        unit_dict = {line[0][:-1]: {sum}}
        result_dict.update(unit_dict)
    print(result_dict)
