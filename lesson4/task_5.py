from functools import reduce

my_data = [el for el in range(100, 1001) if el % 2 == 0]
sum = reduce(lambda x, y: x + y, my_data)
print(sum)
