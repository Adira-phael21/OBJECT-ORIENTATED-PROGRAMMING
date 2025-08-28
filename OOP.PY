# Base Class
class Smartphone:
    # Constructor to initialize attributes
    def __init__(self, brand, model, storage):
        self.brand = brand          # Brand of the phone
        self.model = model          # Model of the phone
        self.storage = storage      # Storage size (GB)

    # Method to simulate making a call
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    # Method to return phone details
    def details(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage"

# Inherited Class (child of Smartphone)
class GamingPhone(Smartphone):
    # Constructor extends base class with new attribute
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)  # Inherit base attributes
        self.cooling_system = cooling_system     # Extra attribute for gaming phones

    # Override details() to add gaming-specific info
    def details(self):
        return super().details() + f" and {self.cooling_system} cooling system"

    # New method specific to GamingPhone
    def play_game(self, game):
        print(f"Playing {game} smoothly on {self.brand} {self.model} 🎮")

# Example Usage
phone1 = Smartphone("Samsung", "S24", 256)          # Create a normal phone
phone2 = GamingPhone("Asus", "ROG Phone 8", 512, "liquid")  # Create a gaming phone

print(phone1.details())   # Show phone details
phone1.call("123456789")  # Make a call

print(phone2.details())   # Show gaming phone details
phone2.play_game("PUBG")  # Play a game
