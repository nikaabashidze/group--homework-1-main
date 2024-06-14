from transport import Transport


class Car(Transport):

    def __init__(self, make: str, model: str, year: int, doors: int):
        super().__init__(make, model, year)
        self.__doors = doors
        self.__validate_doors()

    def __validate_doors(self):
        while self.__doors not in [2, 4]:
            print("Invalid number of doors. Must be either 2 or 4.")
            self.__doors = self.get_doors_input("Enter the number of doors (must be either 2 or 4): ")

    def vehicle_type(self):
        return "Car"

    def __str__(self):
        return f"{super().__str__()} with {self.__doors} doors"

    def __repr__(self):
        return f"{super().__repr__()}, doors={self.__doors}"

    @classmethod
    def create_car(cls):
        make = cls.get_string_input("Enter the brand of the car: ")
        model = input("Enter the model of the car: ")
        year = cls.get_int_input("Enter the year of the car: ")
        doors = cls.get_doors_input("Enter the number of doors (must be either 2 or 4): ")
        return cls(make, model, year, doors)
