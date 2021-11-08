def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort()
    return my_list[-2] + my_list[-1]


print(my_func(a=int(input('Введите первую цифру ')), b=int(input('Введите первую цифру ')),
              c=int(input('Введите первую цифру '))))
