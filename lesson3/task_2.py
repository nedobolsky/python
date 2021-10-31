my_data = {
    'name': input('Введите ваше имя '),
    'surname': input('Введите вашу фамилию '),
    'year_birthd': input('Введите год рождения '),
    'city': input('Введите город проживания '),
    'email': input('Введите ваш email '),
    'telephone_number': input('Введите ваш номер телефона ')
}


def data(**kwargs):
    for key, value in kwargs.items():
        print(value, end=' ')


data(**my_data)
