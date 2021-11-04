from itertools import cycle, count

num = int(input('Ввидет число, для выхода напишите exit - '))
for el in count(int(num)):
    print(el, ' ', end='')
    off_program = input()
    if off_program == 'exit':
        break

my_data = input('Введите элементы через пробел, для добавления в список - ')
my_data = my_data.split()
print('Для выхода напишите exit')
for element in cycle(my_data):
    print(element, ' ', end='')
    off_program = input()
    if off_program == 'exit':
        break
