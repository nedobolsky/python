def division_numbers(a, b):
    try:
        a, b = int(a), int(b)
        result = a / b
    except ValueError:
        return 'Ошибка преобразования типов'
    except ZeroDivisionError:
        return 'Делить на 0 нельзя'
    return result


print(division_numbers(a=input('Введите числитель '), b=input('Введите знаменатель ')))
