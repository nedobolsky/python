class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name}, {self.surname}'

    def get_total_income(self):
        return f'{self.position}, {sum(self._income.values())}'


manager = Position('Leo', 'Travis', 'manager', 10000, 5000)
print(manager.get_full_name())
print(manager.get_total_income())
