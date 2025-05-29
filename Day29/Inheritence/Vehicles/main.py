
"""
9. Vehicle → Car, Bike
Base Class: Vehicle(name, wheels)
Subclasses:
            Car: additional attribute fuel_type
            Bike: additional attribute is_geared
            Override a method description() in both
"""

from Inheritence.Vehicles.Bike import Bike
from Inheritence.Vehicles.Car import Car

car = Car("Audi", 4, "Diesel")
bike = Bike("Bajaj", 2, True)

car.description()
bike.description()