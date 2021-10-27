num = 0
names = []
prices = []
numbers = []
units = []
analytics = {'наименование': names, 'цена': prices, 'количество': numbers, 'ед': units}
base = []

while True:
    element = input('Введите какое количество товаров внести в базу ')
    if element.isdigit():
        break

element = int(element)

while num < element:
    name = input('Введите наименование товара ')
    names.append(name)
    price = input('Введите цену товара ')
    prices.append(price)
    number = input('Введите количество товара ')
    numbers.append(number)
    unit = input('Введите еденицы измерения товара ')
    units.append(unit)
    data = {'наименование': name, 'цена': price, 'количество': number, 'ед': unit}
    num += 1
    tuples = (num, data)
    base.append(tuples)

print(base)
print('\nАналитика:')
for key, value in analytics.items():
    print(key, value)
