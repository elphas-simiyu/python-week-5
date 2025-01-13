# Base class: Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method 'move'")

# Derived class: Car
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Derived class: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Derived class: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# Create instances of each vehicle
car = Car()
plane = Plane()
boat = Boat()

# Call move() method for each instance
print(car.move())   # Output: Driving 🚗
print(plane.move()) # Output: Flying ✈️
print(boat.move())  # Output: Sailing ⛵
