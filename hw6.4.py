class Car:
    def __init__(self):
        self.speed = 100
        self.color = 'Blue'
        self.name = 'SpeedyRacer'
        self.is_police = False

    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')

    def show_speed(self,speed):
        print('Ваша скорость: ',speed)

    def turn(self,direction):
        if direction == 'Left':
            print('Машина повернула налево')
        elif direction == 'Right':
            print('Машина повернула направо')
        else:
            print('Направлени движения задано неверно')
class TownCar(Car):
    def __init__(self):
        super().__init__()
        self.speed = 60

    def show_speed(self,speed):
        print('Ваша скорость: ',speed)
        if speed > 60:
            print('Вы превысили скорость!')

class SportCar(Car):
    def __init__(self):
        super().__init__()
        self.speed = 200


class WorkCar(Car):
    def __init__(self):
        super().__init__()
        self.speed = 40

    def show_speed(self,speed):
        print('Ваша скорость: ',speed)
        if speed > 40:
            print('Вы превысили скорость!')

class PoliceCar(Car):
    def __init__(self):
        super().__init__()
        self.color = 'Black'
        self.is_police = True

police = PoliceCar()
police.go()
police.turn('Right')
police.turn('Left')
police.show_speed(80)
police.stop()
print(police.color)
print(police.is_police)

towncar = TownCar()
towncar.show_speed(80)

workcar = WorkCar()
workcar.show_speed(60)
