from Inheritence.Vehicles.Vehicle import Vehicle


class Bike(Vehicle):
    def __init__(self, name, wheels, is_geared):
        super().__init__(name, wheels)
        self.is_geared = is_geared

    def description(self):
        geared_text = "geared" if self.is_geared else "non-geared"
        print(f"Bike name: {self.name}")
        print(f"Total wheels: {self.wheels}")
        print(f"Gear Type: {geared_text}")