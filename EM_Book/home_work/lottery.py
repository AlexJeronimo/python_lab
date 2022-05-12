from random import choices


class Lottery:
    def __init__(self, list):
        self.list = list

    def get_choice(self):
        c = choices(self.list, k=4)
        for i in c:
            print(i, end=' ')


my_list = [1, 2, 3, 4, 'a', 'b', 'c', 'd']

my_choice = Lottery(my_list)
my_choice.get_choice()
