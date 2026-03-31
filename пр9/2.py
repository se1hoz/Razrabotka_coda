from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling")

# Проверка [cite: 5]
vehicles = [Car(), Bicycle()]
for v in vehicles:
    v.move()
