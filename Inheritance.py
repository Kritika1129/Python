class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)  # Call the base class constructor
        self.fuel_type = fuel_type

    def display_info(self):
        super().display_info()  # Call the display_info of the Vehicle class
        print(f"Fuel type: {self.fuel_type}")

# Example usage
my_car = Car("Toyota", "Corolla", 2020, "Petrol")
my_car.display_info()
print("This program is written by KRITIKA ERP-067")
