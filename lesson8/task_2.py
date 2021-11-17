class DivisionZero:
    def __init__(self, num):
        self.num = num

    def __truediv__(self, other):
        try:
            return self.num / other.num
        except ZeroDivisionError:
            return 'Ошибка. Деление на ноль'


data = DivisionZero(10)
data2 = DivisionZero(2)

print(data / data2)
