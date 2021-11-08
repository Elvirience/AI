i = 0
count = 0
with open('ex3.txt', encoding='UTF-8') as fout:
    for line in fout:
        surname, salary = line.split()
        i += int(salary)
        if int(salary) < 20000:
            print(surname)
        count += 1
    print(f'Средняя величина дохода: {int(i / count)}')