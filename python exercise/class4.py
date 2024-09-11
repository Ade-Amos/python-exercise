class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.make} {self.model}"

# Create an instance and run the method
car1 = Car("Toyota", "Corolla", 2020)
print(car1.description())