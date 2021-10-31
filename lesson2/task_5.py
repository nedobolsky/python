data = [7, 5, 3, 3, 2]

while True:
    num = input('Введите рейтинг ')
    if num.isdigit():
        break

num = int(num)

if num in data:
    number = data.count(num)
    index = data.index(num)
    data.insert(index + number, num)
else:
    for i, k in enumerate(data):
        if num > k:
            data.insert(i, num)
            break
        else:
            continue
    else:
        data.append(num)

print(data)
