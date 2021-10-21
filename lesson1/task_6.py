km_one_day = float(input('Сколько пробежал км в первый день спортсмен '))
day = int(input('На какой день вывести результат '))
num = 1
while num < day:
    km_one_day = round((km_one_day + km_one_day * 0.1), 2)
    num += 1
print(f'На {day}-й день спортсмен достиг результат - не менее {km_one_day} км')
