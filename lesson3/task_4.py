def my_func(a, b):
    try:
        a, b = float(a), int(b)
        if a >= 0 and b < 0:
            return a ** b
        else:
            return 'Введенные числа не соответсвуют условиям'
    except ValueError:
        return 'Ошибка преобразования типов'


print(my_func(a=input('Введите действительное положительное число '), b=input('Введите целое отрицательное число ')))
