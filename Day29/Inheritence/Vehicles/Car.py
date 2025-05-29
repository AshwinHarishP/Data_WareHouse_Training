from Inheritence.Vehicles.Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, name, wheels, fuel_type):
        super().__init__(name, wheels)
        self.fuel_type = fuel_type

    def description(self):
        print(f"Car name: {self.name}")
        print(f"Total wheels: {self.wheels}")
        print(f"Fuel type: {self.fuel_type}")
