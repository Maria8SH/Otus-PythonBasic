from abc import ABC

from homework_02.exceptions import NotEnoughFuel, LowFuelError


class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=1):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Low Fuel")

    def move(self, distance):
        required_fuel = distance * self.fuel_consumption
        if required_fuel <= self.fuel:
            self.fuel -= required_fuel
        else:
            raise NotEnoughFuel("Not Enough Fuel")
