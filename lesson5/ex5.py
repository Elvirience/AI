i = 0
sum = 0
with open('ex5.txt', 'w+', encoding='UTF - 8') as fin:
    fin.write('5 0 1 2 3 7 9 5 6 81 4 56 1')
    fin.seek(0)
    for i in fin.readline().split():
        sum += int(i)
    print(sum)
