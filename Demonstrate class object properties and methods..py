class Car:
    wheels = 4  # Class attribute

    def __init__(self, make, model, year):
        self.make = make  # Instance attribute
        self.model = model
        self.year = year

    def display_info(self):  # Instance method
        print(f"{self.year} {self.make} {self.model}")

    @classmethod
    def is_motor_vehicle(cls):  # Class method
        return True

    @staticmethod
    def honk():  # Static method
        print("Honk!")

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()  # Output: 2020 Toyota Corolla
print("This program is written by KRITIKA ERP-067")
