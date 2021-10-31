data = []

while True:
    el_number = input('Введите кол-во элементов, которые хотите добавить ')
    if el_number.isdigit():
        break

el_number = int(el_number)

while el_number > 0:
    element = input('Введите значения элементов ')
    data.append(element)
    el_number -= 1

for i in range(len(data)):
    if i % 2 != 0:
        continue
    elif len(data) - 1 == i:
        break
    else:
        data[i], data[i + 1] = data[i + 1], data[i]
    i += 2

print(data)
