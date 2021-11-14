class Clothes:
    def __init__(self, size):
        self.size = size

    def footage(self):
        pass

    def __add__(self, other):
        return self.footage + other.footage


class Coat(Clothes):
    @property
    def footage(self):
        return round(self.size / 6.5 + 0.5, 2)


class Costume(Clothes):
    @property
    def footage(self):
        return 2 * self.size + 0.3


coat = Coat(10)
costume = Costume(10)
print(coat.footage)
print(costume.footage)
print(coat + costume)
