from car import Car
from supercar import SuperCar
from van import Van
from bus import Bus
from garage import Garage
from electric_car import ElectricCar


def main():
    garage = Garage()

    while True:
        print("Choose the type of vehicle to create:")
        print("1. Car")
        print("2. SuperCar")
        print("3. Van")
        print("4. Bus")
        print("5. ElectricCar")
        print("6. Display Garage")
        print("7. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            vehicle = Car.create_car()
            garage.add_vehicle(vehicle)
            print(f"Added Car: {vehicle}")
        elif choice == '2':
            vehicle = SuperCar.create_supercar()
            garage.add_vehicle(vehicle)
            print(f"Added SuperCar: {vehicle}")
        elif choice == '3':
            vehicle = Van.create_van()
            garage.add_vehicle(vehicle)
            print(f"Added Van: {vehicle}")
        elif choice == '4':
            vehicle = Bus.create_bus()
            garage.add_vehicle(vehicle)
            print(f"Added Bus: {vehicle}")
        elif choice == '5':
            vehicle = ElectricCar.create_electric_car()
            garage.add_vehicle(vehicle)
            print(f"Added ElectricCar: {vehicle}")
        elif choice == '6':
            garage.display_vehicles()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

        break


if __name__ == "__main__":
    main()
