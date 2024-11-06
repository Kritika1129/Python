class Car:
    def __init__(self, make, model, year):
        self._make = make      # Private attribute
        self._model = model
        self._year = year

    def display_info(self):
        print(f"{self._year} {self._make} {self._model}")

    def set_year(self, year):
        if year > 1885:  # The first car was invented around 1885
            self._year = year
        else:
            print("Invalid year")

# Example usage
my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()  # Output: 2020 Toyota Corolla

# Set a new valid year
my_car.set_year(2021)
my_car.display_info()  # Output: 2021 Toyota Corolla

# Attempt to set an invalid year
my_car.set_year(1800)  # Output: Invalid year
print("This program is written by KRITIKA ERP-067")
