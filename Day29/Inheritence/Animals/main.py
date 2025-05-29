"""
10. Polymorphism with Animals

Base class Animal with method speak()
Subclasses Dog, Cat, Cow override speak() with unique sounds
Call speak() on each object in a loop
"""
from Inheritence.Animals.Cat import Cat
from Inheritence.Animals.Cow import Cow
from Inheritence.Animals.Dog import Dog

animals = [Dog(), Cat(), Cow()]

# Loop through and call speak()
for animal in animals:
    print(animal.speak())
