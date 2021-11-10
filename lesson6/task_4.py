class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} машина поехала')

    def stop(self):
        print(f'{self.name} машина остановилась')

    def turn(self, direction):
        print(f"{self.name} машина повернула {'налево' if direction == 'left' else 'right'}")

    def show_speed(self):
        print(f'Машина едет со скоростью {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'{self.name} превышение скорости' if self.speed > 60 else 'Скорость в норме')


class SportCar(Car):
    def name_car(self):
        print(f'{self.name} - спортивный автомобиль')


class WorkCar(Car):
    def show_speed(self):
        print(f'{self.name} превышение скорости' if self.speed > 40 else 'Скорость в норме')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


ferrari = WorkCar(80, 'Red', 'ferrari')
ferrari.go()
ferrari.show_speed()
ferrari.turn('left')
ferrari.stop()

police = PoliceCar(100, 'White', 'Police')
police.go()
police.show_speed()


