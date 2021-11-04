from random import randrange

i=0
new_list = []
len_list = randrange(20)
my_gen = [randrange(20) for i in range(len_list)]
print(my_gen)
try:
    while i != (len_list - 1):
        if my_gen[i] < my_gen[i + 1]:
            new_list.append(my_gen[i + 1])
        i += 1
except IndexError:
    print(new_list)
else:
    print(new_list)
