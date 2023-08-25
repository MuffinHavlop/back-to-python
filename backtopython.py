class Car():
    def __init__(self, colour, model, year):
        self.colour = colour
        self.model = model
        self.year = year

class Tesla(Car):
    def __init__(self, colour, model, year, engine, energy):
        super().__init__(colour, model, year)
        self.engine = engine
        self.energy = energy

class Ford(Car):
    def __init__(self, colour, model, year, gas_engine, fuel):
        super().__init__(colour, model, year)
        self.gas_engine = gas_engine
        self.fuel = fuel


Elon_Musk = Tesla("Gray", "CyberTruck", 2023, "Simple engine", "Electric")
Jim_Farley = Ford("Blue", "F-150", 1975, "Fairly simple engine", "Gasoline")

print(Elon_Musk.colour)
print(Elon_Musk.model)
print(Jim_Farley.colour)
print(Jim_Farley.model)
