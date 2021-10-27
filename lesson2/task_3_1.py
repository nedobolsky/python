while True:
    num = input('Введите цифру месяца ')
    if num.isdigit():
        break

num = int(num)

winter_list = [12, 1, 2]
spring_list = [3, 4, 5]
summer_list = [6, 7, 8]
autumn_list = [9, 10, 11]

if num in winter_list:
    print('Зима')
elif num in spring_list:
    print('Весна')
elif num in summer_list:
    print('Лето')
else:
    print('Осень')
