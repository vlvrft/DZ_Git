class Car:
    is_police = False

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.speed = 0

    def show_speed(self):
        print(f'Current vehicle speed {self.speed} mp/h')

    def go(self, speed=35):
        self.speed = speed
        print(f'The car moved at a speed {self.speed} mp/h')

    def stop(self):
        self.speed = 0
        print(f'The Car Stopped')

    def turn(self, direction):
        if direction == "right" or direction == "left" or direction == "reversal":
            print(f'The car made a maneuver {direction}')
        else:
            print("Crash!")


class TownCar(Car):
    def show_speed(self):
        if self.speed >= 61:
            print(f'Over speed')
        else:
            print(f'Permissible speed')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 41:
            print(f'Over speed')
        else:
            print(f'Permissible speed')


class PoliceCar(Car):
    is_police = True


auto_1 = PoliceCar('black', 'Chevrolet')
auto_1.go(20)
auto_2 = SportCar('red', 'Lamborghini')
auto_2.go(80)
auto_2.show_speed()
auto_2.turn("right")
auto_2.turn("bounce")
auto_3 = WorkCar('blue', 'Gazel')
auto_3.go(42)
auto_3.show_speed()
auto_4 = TownCar('white', 'BMW')
auto_4.go(60)
auto_4.show_speed()
