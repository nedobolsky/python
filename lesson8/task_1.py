class Data:
    times = input('Введите дату через тиреб например: 17-11-2021 - ')

    @classmethod
    def time_str_int(cls):
        cls.times = list(map(int, cls.times.split('-')))
        return cls.times

    @staticmethod
    def valid_data(days, months, years):
        day = range(0, 32)
        month = range(0, 13)
        year = range(0, 2100)
        if days in day and months in month and years in year:
            return 'Вы ввели коректную дату'
        else:
            'Ошибка, дата не корректная'


print(Data.time_str_int())
print(Data.valid_data(17, 11, 2021))
