class ComplexMumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if self.b + other.b > 0:
            return f'z = {self.a + other.a}+{self.b + other.b}i'
        else:
            return f'z = {self.a + other.a}{self.b + other.b}i'

    def __mul__(self, other):
        if self.a * other.b + self.b * other.a > 0:
            return f'z = {self.a * other.a - self.b * other.b}+{self.a * other.b + self.b * other.a}i'
        else:
            return f'z = {self.a * other.a - self.b * other.b}{self.a * other.b + self.b * other.a}i'


number = ComplexMumber(2, 2)
number_two = ComplexMumber(-4, 3)
print(number + number_two)
print(number * number_two)
