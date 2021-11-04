from random import randrange

len_gen = randrange(20)
gen = [randrange(20) for i in range(len_gen)]
print(gen)
new_gen = [el for el in gen if gen.count(el) == 1]
print(new_gen)
