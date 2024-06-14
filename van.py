from transport import Transport


class Van(Transport):
    def __init__(self, make: str, model: str, year: int, cargo_space: float):
        super().__init__(make, model, year)
        self._cargo_space = cargo_space
        self.__validate_cargo_space()

    def __validate_cargo_space(self):
        while not (0 < self._cargo_space <= 1000):
            print("Invalid cargo space. Cargo space must be between 0 and 1000 cubic meters.")
            self._cargo_space = self.get_cargo_space_input("Enter the cargo space "
                                                           "(must be between 0 and 1000 cubic meters): ")

    def vehicle_type(self):
        return "Van"

    def __str__(self):
        return f"{super().__str__()} with {self._cargo_space} cubic meters of cargo space"

    def __repr__(self):
        return f"{super().__repr__()}, cargo_space={self._cargo_space}"

    @classmethod
    def create_van(cls):
        make = cls.get_string_input("Enter the brand of the van: ")
        model = input("Enter the model of the van: ")
        year = cls.get_int_input("Enter the year of the van: ")
        cargo_space = cls.get_cargo_space_input("Enter the cargo space in cubic meters (must be between 0 and 1000): ")
        return cls(make, model, year, cargo_space)
