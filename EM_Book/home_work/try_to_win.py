from random import choices


class TryToWin:
    def __init__(self, lottery):
        self.lottery = lottery

    def try_to_win(self):
        count = 0
        alphabet_and_numeric = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                                'Z']
        try_to = ''
        while try_to != self.lottery:
            try_to = ''.join(choices(alphabet_and_numeric, k=len(self.lottery)))
            count += 1
        print(count)


my_lottery = TryToWin('ABch')
my_lottery.try_to_win()
