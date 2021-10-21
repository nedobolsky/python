second_time = int(input('Введите время в секундах '))
second = second_time % 60
minute = second_time / 60 % 60
hour = second_time / 3600 % 60
print(f'{int(hour):02}:{int(minute):02}:{second:02}')
