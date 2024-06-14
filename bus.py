from transport import Transport


class Bus(Transport):
    def __init__(self, make: str, model: str, year: int, capacity: int):
        super().__init__(make, model, year)
        self._capacity = capacity
        self.__validate_capacity()

    def __validate_capacity(self):
        while not (10 <= self._capacity <= 100):
            print("Invalid capacity. Capacity must be between 10 and 100.")
            self._capacity = self.get_capacity_input("Enter the capacity of the bus (must be between 10 and 100): ")

    def vehicle_type(self):
        return "Bus"

    def __str__(self):
        return f"{super().__str__()} with a capacity of {self._capacity} passengers"

    def __repr__(self):
        return f"{super().__repr__()}, capacity={self._capacity}"

    @classmethod
    def create_bus(cls):
        make = cls.get_string_input("Enter the make of the bus: ")
        model = input("Enter the model of the bus: ")
        year = cls.get_int_input("Enter the year of the bus: ")
        capacity = int(input("Enter the capacity of the bus: "))
        return cls(make, model, year, capacity)
