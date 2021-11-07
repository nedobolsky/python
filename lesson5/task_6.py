my_dict = {}
with open('data6.txt', 'r', encoding='utf-8') as file:
    for line in file:
        item, hours = line.split(':')
        hour = [el for el in hours if (el >= '0' and el <= '9') or el == ' ']
        element = sum(map(int, ''.join(hour).split()))
        my_dict[item] = element
    print(my_dict)