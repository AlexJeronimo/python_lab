from random import randint


class Die:
    def __init__(self):
        self.sides = 6
        self.rolls = 10

    def set_sides(self):
        self.sides = int(input("Set die sides: "))

    def set_rolls(self):
        self.rolls = int(input("Set number of rolls: "))

    def roll_die(self):
        while self.rolls != 0:
            print(randint(1, self.sides))
            self.rolls -= 1


my_die = Die()
my_die.set_sides()
my_die.set_rolls()
my_die.roll_die()


