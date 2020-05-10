
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        request = ""

        while request not in moves:
            request = input("Rock, paper, scissors? >").lower()

        return request


# ReflectPlayer class
class ReflectPlayer(Player):
        # reflect = "rock"
        reflect = random.choice(moves)

        def move(self):
            return self.reflect

        def learn(self, my_move, their_move):
            self.reflect = their_move


class CyclePlayer(Player):
    # cycle = 'rock'
    cycle =random.choice(moves)

    def move(self):
        return self.cycle

    def learn(self, my_move, their_move):
        if my_move == 'rock':
            self.cycle = 'paper'
        elif my_move == 'paper':
            self.cycle = 'scissors'
        elif my_move == 'scissors':
            self.cycle = 'rock'


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        # print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if move1 is not None:
            print(f"You played {move1}.\nOpponent played {move2}.")


            if self.p1.beats(move1, move2) == True:
                print("** PLAYER ONE WINS **")
                # print(f"This Round : Player 1 WIN")
                self.p1_score += 1
                print(f"Score: Player One {self.p1_score},"
                        f"Player Two {self.p2_score}")

            elif self.p2.beats(move2, move1) == True:
                print("** PLAYER TWO WINS **")
                # print(f"This Round : Player 2 WIN")
                self.p2_score += 1
                print(f"Score: Player One {self.p1_score},"
                        f"Player Two {self.p2_score}")

            else:
                print("** TIE **")
                print(f"Score: Player One {self.p1_score},"
                        f"Player Two {self.p2_score}")

        # elif move1 == move2:
        #     print("This Round : TIE")
        # else:
        #     print("Wrong Input !")
        # self.p1.learn(move1, move2)
        # self.p2.learn(move2, move1)

    def play_game(self):
        # print("Game start!")
        print("Rock Paper Scissors, Go!")
        for round in range(3):
            print(f"\nRound {round} --")
            self.play_round()
        # print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
