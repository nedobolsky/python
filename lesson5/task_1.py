with open('data.txt', 'w') as file:
    while True:
        my_data = input('Введите данные - ')
        if my_data:
            file.write(f'{my_data}\n')
        else:
            break