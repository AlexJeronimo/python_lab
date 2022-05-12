# from car import Car, ElectricCar

# my_beetle = Car('Volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = ElectricCar('tesla', 'roadster', 2020)
# print(my_tesla.get_descriptive_name())


# import car
# my_beetle = car.Car('Volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = car.ElectricCar('tesla', 'roadster', 2020)
# print(my_tesla.get_descriptive_name())


# from car import Car
# from electric_car import ElectricCar
#
# my_beetle = Car('Volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = ElectricCar('tesla', 'roadster', 2020)
# print(my_tesla.get_descriptive_name())

from electric_car import ElectricCar as EC
my_tesla = EC('tesla', 'model Y', 2017)
print(my_tesla.get_descriptive_name())
