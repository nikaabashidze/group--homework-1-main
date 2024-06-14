import pickle


class Garage:
    def __init__(self):
        self.vehicles = {}
        self.load_from_file()  # Load previously saved garage

    def add_vehicle(self, vehicle):
        vehicle_id = f"{vehicle.vehicle_type()}_{len(self.vehicles) + 1}"
        self.vehicles[vehicle_id] = vehicle
        self.save_to_file()  # Save updated garage

    def display_vehicles(self):
        if not self.vehicles:
            print("The garage is empty.")
        else:
            print("Vehicles in the garage:")
            for vehicle_id, vehicle in self.vehicles.items():
                print(f"{vehicle_id}: {vehicle}")

    def save_to_file(self):
        with open('garage.pkl', 'wb') as file:
            pickle.dump(self.vehicles, file)

    def load_from_file(self):
        try:
            with open('garage.pkl', 'rb') as file:
                self.vehicles = pickle.load(file)
        except FileNotFoundError:
            self.vehicles = {}

    def __del__(self):
        self.save_to_file()  # Save garage state when object is deleted
