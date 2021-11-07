with open('data2.txt', 'r') as file:
    data_str = 0
    while True:
        my_data = file.readline().split()
        data_words = len(my_data)
        if not my_data:
            break
        data_str += 1
        print(f'В строке {data_str}, находится {data_words} слов(а)')
    print(f'Всего строк в файле - {data_str}')
