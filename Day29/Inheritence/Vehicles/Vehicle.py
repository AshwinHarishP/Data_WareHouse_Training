class Vehicle:
    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels

    def description(self):
        print(f"Vehicle name: {self.name}")
        print(f"Total wheels: {self.wheels}")

