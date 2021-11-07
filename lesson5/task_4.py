my_data = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('data4new.txt', 'w', encoding='utf-8') as file_new:
    with open('data4.txt', 'r', encoding='utf-8') as file:
        for line in file:
            data = line.split()
            file_new.write(line.replace(data[0], my_data.get(data[0])))
