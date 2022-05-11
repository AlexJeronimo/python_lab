# 9.1


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name.title()} has {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name.title()} is open now.")


toti = Restaurant('Toti', 'hell')

print(f"The restaurant name is {toti.restaurant_name}")
print(f"The cuisine type is {toti.cuisine_type}")

toti.describe_restaurant()
toti.open_restaurant()

# 9.2

ameli = Restaurant('Ameli', 'Big Bob')
ameli.describe_restaurant()
freddy_fries = Restaurant('Freddy Fries', '"huge cuisine"')
freddy_fries.describe_restaurant()
olaf = Restaurant('Olaf Burgers', 'small')
olaf.describe_restaurant()


# 9.3
class User:
    def __init__(self, first_name, last_name, job_title, room):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.room = room

    def describe_user(self):
        print(f"The User {self.first_name} {self.last_name} works as {self.job_title} in {self.room} room")

    def greet_user(self):
        print(f"{self.first_name} {self.last_name} Welcome to our company in {self.job_title} role.")


bob = User('Bob', 'Parker', 'accountant', 47)
bob.describe_user()
bob.greet_user()

syu = User('Syu', 'Elliot', 'sales manager', 13)
syu.describe_user()
syu.greet_user()

