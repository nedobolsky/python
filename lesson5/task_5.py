from functools import reduce

with open('data5.txt', 'w+') as file:
    data = [str(x) for x in range(1, 4)]
    file.write(' '.join(data))
    file.seek(0)
    print(f'Сумма всех чисел = {reduce(lambda x, y: int(x) + int(y), file.readline().split())}')
