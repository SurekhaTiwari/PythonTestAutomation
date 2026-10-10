
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def walk(self):
        print(f"{self.name} is walking.")

    def run(self):
        print(f"{self.name} is running.")

    def eat(self,food):
        print(f"{self.name} is eating {food}.")

    @abstractmethod
    def make_sound(self):
        pass

    def __str__(self):
        return f"Animal: {self.name}, Age: {self.age}"

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says Meow!")