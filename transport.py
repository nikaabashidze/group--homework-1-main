from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, make: str, model: str, year: int):
        self._make = make
        self._model = model
        self._year = year

    @abstractmethod
    def vehicle_type(self):
        pass

    def __str__(self):
        return f"{self._make} {self._model} ({self._year})"

    def __repr__(self):
        return f"{self.__class__.__name__}(make='{self._make}', model='{self._model}', year={self._year})"

    @staticmethod
    def get_string_input(prompt):
        while True:
            value = input(prompt)
            if value.isalpha():
                return value
            else:
                print("Invalid input. Please enter a valid string.")

    @staticmethod
    def get_int_input(prompt):
        while True:
            value = input(prompt)
            if value.isdigit():
                return int(value)
            else:
                print("Invalid input. Please enter a valid integer.")

    @staticmethod
    def get_doors_input(prompt):
        doors = None
        while doors not in [2, 4]:
            doors = Transport.get_int_input(prompt)
            if doors not in [2, 4]:
                print("Invalid number of doors. Must be either 2 or 4.")
        return doors

    @staticmethod
    def get_top_speed_input(prompt):
        top_speed = None
        while top_speed is None or not (1 <= top_speed <= 500):
            try:
                top_speed = int(input(prompt))
                if not (1 <= top_speed <= 500):
                    print("Invalid top speed. Top speed must be between 1 and 500.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        return top_speed

    @staticmethod
    def get_cargo_space_input(prompt):
        cargo_space = None
        while cargo_space is None or not (0 < cargo_space <= 1000):
            try:
                cargo_space = float(input(prompt))
                if not (0 < cargo_space <= 1000):
                    print("Invalid cargo space. Cargo space must be between 0 and 1000 cubic meters.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        return cargo_space

    @staticmethod
    def get_battery_capacity_input(prompt):
        battery_capacity = None
        while battery_capacity is None or not (0 <= battery_capacity <= 100):
            try:
                battery_capacity = int(input(prompt))
                if not (0 <= battery_capacity <= 100):
                    print("Invalid battery capacity. Battery capacity must be between 0% and 100%.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        return battery_capacity
