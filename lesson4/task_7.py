n = int(input('Введите до какого числа подсчитать факториал числа '))


def fact(num):
    f_num = 1
    for i in range(1, num + 1):
        f_num *= i
        yield f'{i}! = {f_num}'


for el in fact(n):
    print(el)
