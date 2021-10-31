def sum_numbers():
    sum_number = 0
    while True:
        my_list = input('Введите числа разделеные пробелом, в программе можно использовать любые спецсимволы ').split()
        for i in my_list:
            if not i.isdigit():
                return sum_number
            else:
                try:
                    i = int(i)
                    sum_number += i
                except ValueError:
                    return 'ошибка'
        print(sum_number)


print(sum_numbers())
