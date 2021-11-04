from sys import argv

name, hours, money_in_hour, prize = argv
salary = int(money_in_hour) * int(hours) + int(prize)
print(salary)
print(f'Заработная плата: {salary}')
