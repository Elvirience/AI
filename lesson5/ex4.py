i = 0
fout = open('ex4.txt', encoding='UTF-8')
fin = open('ex4_in.txt', 'w', encoding='UTF-8')
my_list = ['Один', 'Два', 'Три', 'Четыре']
for line in fout:
    line = line.split(' - ')
    line[0] = my_list[i]
    fin.write(' - '.join(line))
    i += 1
fout.close()
fin.close()
