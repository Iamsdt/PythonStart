import src.practice.oop.Car as Car
import src.practice.oop.SuperCar as SuperCar

car = Car.Car("Tata", 2018, 300, 20)
car.details()
print("Run car")
car.run(12)
car.fuelStatus()

print("\n\nNew Car")

car2 = SuperCar.SuperCar("Tesla", 2016, 400, 200, "red")
car2.details()
print("Run car")
car2.run(120)
car2.fuelStatus()
