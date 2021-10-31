def my_func(a, b):
    try:
        a, b = float(a), int(b)
        if a >= 0 and b < 0:
            b = abs(b)
            to_extend = a
            for i in range(1, b):
                to_extend = to_extend * a
            return 1 / to_extend
        else:
            return 'Введенные числа не соответсвуют условиям'
    except ValueError:
        return 'Ошибка преобразования типов'


print(my_func(a=input('Введите действительное положительное число '), b=input('Введите целое отрицательное число ')))
