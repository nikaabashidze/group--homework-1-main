from car import Car
from electric_mixin import ElectricMixin


class ElectricCar(Car, ElectricMixin):
    def __init__(self, make: str, model: str, year: int, doors: int, battery_capacity: int):
        Car.__init__(self, make, model, year, doors)
        ElectricMixin.__init__(self, battery_capacity)

    def __str__(self):
        return f"{super(Car, self).__str__()} and a battery capacity of {self._battery_capacity} kWh"

    def __repr__(self):
        return f"{super(Car, self).__repr__()}, battery_capacity={self._battery_capacity}"

    @classmethod
    def create_electric_car(cls):
        make = cls.get_string_input("Enter the make of the ElectricCar: ")
        model = input("Enter the model of the ElectricCar: ")
        year = cls.get_int_input("Enter the year of the ElectricCar: ")
        doors = cls.get_doors_input("Enter the number of doors (must be either 2 or 4): ")
        battery_capacity = cls.get_battery_capacity_input("Enter the battery capacity (must be between 0% and 100%): ")
        return cls(make, model, year, doors, battery_capacity)
