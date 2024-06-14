from transport import Transport


class ElectricMixin:
    def __init__(self, battery_capacity: int):
        self._battery_capacity = battery_capacity
        self.__validate_battery_capacity()

    def __validate_battery_capacity(self):
        while not (0 <= self._battery_capacity <= 100):
            print("Invalid battery capacity. Battery capacity must be between 0% and 100%.")
            self._battery_capacity = Transport.get_battery_capacity_input(
                "Enter the battery capacity (must be between 0% and 100%): ")

    def charge(self):
        return f"Charging the battery with capacity {self._battery_capacity} kWh."

#     კომპოზიცია და მიქსინგი
