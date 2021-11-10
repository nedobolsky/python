class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass_asphalt(self):
        return f'{(self._length * self._width * 25 * 5) / 1000} тонн '


asp_road = Road(5000, 20)
print(asp_road.calc_mass_asphalt())
