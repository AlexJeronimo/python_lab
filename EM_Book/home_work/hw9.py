# 9.1


# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(f"The restaurant {self.restaurant_name.title()} has {self.cuisine_type} cuisine.")
#
#     def open_restaurant(self):
#         print(f"The restaurant {self.restaurant_name.title()} is open now.")
#
#
# toti = Restaurant('Toti', 'hell')
#
# print(f"The restaurant name is {toti.restaurant_name}")
# print(f"The cuisine type is {toti.cuisine_type}")
#
# toti.describe_restaurant()
# toti.open_restaurant()

# 9.2

# ameli = Restaurant('Ameli', 'Big Bob')
# ameli.describe_restaurant()
# freddy_fries = Restaurant('Freddy Fries', '"huge cuisine"')
# freddy_fries.describe_restaurant()
# olaf = Restaurant('Olaf Burgers', 'small')
# olaf.describe_restaurant()


# 9.3
# class User:
#     def __init__(self, first_name, last_name, job_title, room):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.job_title = job_title
#         self.room = room
#
#     def describe_user(self):
#         print(f"The User {self.first_name} {self.last_name} works as {self.job_title} in {self.room} room")
#
#     def greet_user(self):
#         print(f"{self.first_name} {self.last_name} Welcome to our company in {self.job_title} role.")
#
#
# bob = User('Bob', 'Parker', 'accountant', 47)
# bob.describe_user()
# bob.greet_user()
#
# syu = User('Syu', 'Elliot', 'sales manager', 13)
# syu.describe_user()
# syu.greet_user()

# 9.4

# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(f"The restaurant {self.restaurant_name.title()} has {self.cuisine_type} cuisine.")
#
#     def open_restaurant(self):
#         print(f"The restaurant {self.restaurant_name.title()} is open now.")
#
#     def set_number_served(self, clients):
#         self.number_served = clients
#
#     def get_number_served(self):
#         print(f"Now served {self.number_served} places")
#
#     def increment_number_served(self, clients):
#         self.number_served += clients
#
#
# my_restaurant = Restaurant('Alex Beef', 'hell')
#
# my_restaurant.open_restaurant()
#
# my_restaurant.set_number_served(10)
# my_restaurant.get_number_served()
#
# my_restaurant.increment_number_served(15)
# my_restaurant.get_number_served()


# 9.5

# class User:
#     def __init__(self, first_name, last_name, job_title, room):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.job_title = job_title
#         self.room = room
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print(f"The User {self.first_name} {self.last_name} works as {self.job_title} in {self.room} room")
#
#     def greet_user(self):
#         print(f"{self.first_name} {self.last_name} Welcome to our company in {self.job_title} role.")
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#         print(f"Your login attempts was reset and now is {self.login_attempts}")
#
#     def get_login_attempts(self):
#         return self.login_attempts
#
# new_user = User('Bob', 'Kalahan', ' CEO', 101)
# new_user.increment_login_attempts()
# print(new_user.get_login_attempts())
#
# new_user.reset_login_attempts()
# print(new_user.get_login_attempts())


# 9.6

# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(f"The restaurant {self.restaurant_name.title()} has {self.cuisine_type} cuisine.")
#
#     def open_restaurant(self):
#         print(f"The restaurant {self.restaurant_name.title()} is open now.")
#
#     def set_number_served(self, clients):
#         self.number_served = clients
#
#     def get_number_served(self):
#         print(f"Now served {self.number_served} places")
#
#     def increment_number_served(self, clients):
#         self.number_served += clients
#
#
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name):
#         self.restaurant_name = restaurant_name
#         self.flavors = 'vanilla'
#
#     def set_flavor(self):
#         self.flavors = input("What flavor do you want? ")
#
#     def get_ice_cream(self):
#         print(f"You chose an ice cream with a {self.flavors}")
#
#
# ice_cream = IceCreamStand('Hallil')
# ice_cream.open_restaurant()
# ice_cream.set_flavor()
# ice_cream.get_ice_cream()

# 9.7 - 9.8

# class User:
#     def __init__(self, first_name, last_name, job_title, room):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.job_title = job_title
#         self.room = room
#
#     def describe_user(self):
#         print(f"The User {self.first_name} {self.last_name} works as {self.job_title} in {self.room} room")
#
#     def greet_user(self):
#         print(f"{self.first_name} {self.last_name} Welcome to our company in {self.job_title} role.")
#
#
# class Privileges:
#     def __init__(self):
#         self.privileges = []
#
#     def set_privileges(self):
#         q = False
#         while not q:
#             print("Type an privilege you want to assign to Admin user role. For exit type 'q': ")
#             p = input()
#             if p == 'q':
#                 q = True
#             else:
#                 self.privileges.append(p)
#
#     def get_privileges(self):
#         print(f"Admin has privileges: {[i for i in self.privileges]}")
#
#
# class Admin(User):
#     def __init__(self, first_name, last_name, job_title, room):
#         super().__init__(first_name, last_name, job_title, room)
#         self.privileges = Privileges()
#
#
# admin = Admin('Alex', 'Jeronimo', 'admin', 103)
# admin.privileges.set_privileges()
# admin.privileges.get_privileges()


# 9.9

# class Car:
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} kilometers on it")
#
#     def update_odometer(self, kilometers):
#         if kilometers >= self.odometer_reading:
#             self.odometer_reading = kilometers
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, kilometers):
#         self.odometer_reading += kilometers
#
#     def fill_gas_tank(self):
#         pass
#
#
# class Battery:
#     def __init__(self, battery_size=75):
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}-kWh battery")
#
#     def get_range(self):
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315
#         print(f"This car can go about {range} kilometers on a full charge")
#
#     def upgrade_battery(self):
#         self.battery_size = 100
#
#
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()
#
#     def fill_gas_tank(self):
#         print("This car doesn't need a gas tank")
#
#
# my_tesla = ElectricCar('tesla', 'model s', 2022)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

# 9.10

# from restaurant import Restaurant
# my_restaurant = Restaurant('Kenobi', 'hell')
# print(my_restaurant.open_restaurant())

# 9.11-12


# import privileges
#
# admin = privileges.Admin('Alex', 'Jeronimo', 'admin', 103)
# admin.privileges.get_privileges()

# 9.13 - 14 - 15

