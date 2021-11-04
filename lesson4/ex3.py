gen = (i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0)
for el in gen:
    print(el)
