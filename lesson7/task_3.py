class Cell:

    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        return self.param + other.param

    def __sub__(self, other):
        if (self.param - other.param) > 0:
            return self.param - other.param
        else:
            return 'Разность двух клеток меньше нуля'

    def __mul__(self, other):
        return self.param * other.param

    def __truediv__(self, other):
        return round(self.param / other.param)

    def make_order(self, element):
        try:
            return '\n'.join(['*' * element for _ in range(self // element)]) + '\n' + '*' * (self % element)
        except TypeError:
            return 'Метод "make_order" не работает. Возможно у вас получилось отрицательное число.'


cell = Cell(5)
cell_two = Cell(8)
result = cell - cell_two
print(result, '\n')
print(Cell.make_order(result, 5), end='')
