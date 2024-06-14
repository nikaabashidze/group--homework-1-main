from car import Car


class SuperCar(Car):
    def __init__(self, make: str, model: str, year: int, doors: int, top_speed: int):
        super().__init__(make, model, year, doors)
        self.__top_speed = top_speed
        self.__validate_top_speed()

    def __validate_top_speed(self):
        while not (1 <= self.__top_speed <= 500):
            print("Invalid top speed. Top speed must be between 1 and 500.")
            self.__top_speed = self.get_top_speed_input("Enter the top speed (must be between 1 and 500): ")

    def vehicle_type(self):
        return "SuperCar"

    def __str__(self):
        return f"{super().__str__()}  top speed - {self.__top_speed} km/h"

    def __repr__(self):
        return f"{super().__repr__()}, top_speed={self.__top_speed}"

    @classmethod
    def create_supercar(cls):
        make = cls.get_string_input("Enter the brand of the supercar: ")
        model = input("Enter the model of the supercar: ")
        year = cls.get_int_input("Enter the year of the supercar: ")
        doors = cls.get_doors_input("Enter the number of doors (must be either 2 or 4): ")
        top_speed = SuperCar.get_top_speed_input("Enter the top speed of the supercar (must be between 1 and 500): ")
        return cls(make, model, year, doors, top_speed)
