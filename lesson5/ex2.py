lines = 0
words = 0
fout = open('ex2.txt', encoding='UTF-8')
for i in fout.readlines():
    print(f"Число слов в строке {lines + 1}: {len(i.split())}")
    lines += 1
print(f'Число строк: {lines}')
fout.close()
