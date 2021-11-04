data = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 800]
my_data = [data[el] for el in range(len(data) - 1) if data[el] > data[el - 1]]
print(my_data)
