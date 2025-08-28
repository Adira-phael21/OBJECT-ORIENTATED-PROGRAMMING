# Parent class
class Vehicle:
    # Method to be overridden by child classes
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Child classes implementing their own move()
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Example Usage
vehicles = [Car(), Plane(), Boat()]  # Store all vehicle objects in a list

for v in vehicles:
    v.move()  # Each class runs its own version of move()
