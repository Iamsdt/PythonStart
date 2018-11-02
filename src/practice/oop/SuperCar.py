import src.practice.oop.Car as Car


class SuperCar(Car.Car):

    _rate = .8

    def __init__(self, name, year, cc, fuel, color):
        super(SuperCar, self).__init__(name, year, cc, fuel)
        self.color = color

    def run(self, time):
        temp = time * self._rate
        self._fuel -= temp

    def details(self):
        super(SuperCar, self).details()
        print("Color:" + self.color)

    def getColor(self):
        print("Color:" + self.color)
