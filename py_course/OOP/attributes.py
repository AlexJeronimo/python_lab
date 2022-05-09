class Car:

    wheels_number = 4

    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed


mazda_car = Car(name='Mazda CX7', color='Grey', year=2017, is_crashed=True)
print(mazda_car.name, mazda_car.color, mazda_car.year, mazda_car.is_crashed)

bmw_car = Car(name='BMW', color='Red', year='2020',is_crashed=False)
print(bmw_car.name, bmw_car.color, bmw_car.year, bmw_car.wheels_number)
