class Car:
    _fuel = 0.0

    _rate = 0.2

    def __init__(self, name, year, cc, fuel):
        self.name = name
        self.year = year
        self.cc = cc
        self._fuel = fuel

    def add_fuel(self, amount):
        self._fuel += amount

    def run(self, time):
        temp = time * self._rate
        self._fuel -= temp

    def fuelStatus(self):
        print("Current Fuel: ", self._fuel)

    def details(self):
        print("Name: " + self.name + "\nYear:" + str(self.year)
              + "\nCC:" + str(self.cc) + "\nCurrent Fuel:" + str(self._fuel))
