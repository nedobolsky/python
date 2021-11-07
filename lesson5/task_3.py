with open('data3.txt', 'r', encoding='utf-8') as file:
    my_data = {line.split()[0]: int(line.split()[1]) for line in file}
    print(f'Средняя заработная плата: {sum(my_data.values()) / len(my_data)}')
    print(f'Заработная плата меньше 20тыс. у работника - {[surname for surname, salary in my_data.items() if salary < 20000]}')


