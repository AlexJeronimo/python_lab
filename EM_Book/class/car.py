"""Class to model car"""


class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} kilometers on it")

    def update_odometer(self, kilometers):
        if kilometers >= self.odometer_reading:
            self.odometer_reading = kilometers
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, kilometers):
        self.odometer_reading += kilometers


# my_new_car = Car('audi', 'q7', 2020)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
#
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
#
# my_new_car.update_odometer(45)
# my_new_car.read_odometer()
#
# my_new_car.update_odometer(17)
# my_new_car.read_odometer()
#
# my_used_car = Car('subaru', 'outback', 2017)
# print(my_used_car.get_descriptive_name())
#
# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
