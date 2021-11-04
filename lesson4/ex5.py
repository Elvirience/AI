from functools import reduce

gen = [i for i in range(100, 1001) if i % 2 == 0]
print(gen)
print(reduce(lambda a, b: a * b, gen))
