proceeds = int(input('Введите значение выручки компании '))
my_cos = int(input('Введите значение издержек компании '))
result = proceeds - my_cos
if result > 0:
    print('Компания работает с прибылью')
    employee = int(input('Введите количество сотрудников '))
    profitability = result / proceeds
    proceeds_on_employee = proceeds / employee
    print('Рентабельность компании =', profitability)
    print('Вклад каждого сотрудника в выручки =', proceeds_on_employee)
elif result == 0:
    print('Компания сработала в ноль')
else:
    print('Компания работает в убыток')
