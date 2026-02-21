from Heater import Heater


class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.heater = Heater()

    def break_(self):
        print(f"Car {self.model} stopped.")

    def turnHeaterOn(self, temp=25):
        self.heater.on()
        self.heater.reachRequestedTemp(temp)


car1 = Car("BMW-X6", 2019, "black")
car1.turnHeaterOn(26)
