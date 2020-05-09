
import random
moves  = ['rock', 'paper', 'scissors']

class player():
    # """docstring for Player."""

    def __init__(self):
        # super(Player, self).__init__()
        self.initalScore = Random.start(self)


class Random(player):
    def start():
        return random.choice(moves)

test = Random.start()
print (test)
