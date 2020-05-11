
# Editor: Khalid
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


# Main Class "Player"
class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    # Chick Who wins the game
    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


# subclasses starting with RandomPlayer
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# HumanPlayer subclass
class HumanPlayer(Player):
    def move(self):
        request = ""

        # loop till the valid move
        while request not in moves:
            request = input("Rock, paper, scissors? >").lower()

        return request


# ReflectPlayer subclass
class ReflectPlayer(Player):
    # reflect = "rock"
    reflect = random.choice(moves)

    # selecting the last move
    def move(self):
        return self.reflect

    # saving the last move
    def learn(self, my_move, their_move):
        self.reflect = their_move


class CyclePlayer(Player):
    # cycle = 'rock'
    cycle = random.choice(moves)

    def move(self):
        return self.cycle

    # doing cycle you can do it with an array, but its only 3 elements!
    def learn(self, my_move, their_move):
        if my_move == 'rock':
            self.cycle = 'paper'
        elif my_move == 'paper':
            self.cycle = 'scissors'
        elif my_move == 'scissors':
            self.cycle = 'rock'


class Game:
    # Initial values and scores
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    # Stat new round!
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        # print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        # Loop as long as it's not None, no need for more conditionals check
        # HumanPlayer move method
        if move1 is not None:
            print(f"You played {move1}.\nOpponent played {move2}.")

            # Determine the scores using beats method
            if self.p1.beats(move1, move2):  # or is True
                print("** PLAYER ONE WINS **")
                # print(f"This Round : Player 1 WIN")
                self.p1_score += 1
                print(f"Score: Player One {self.p1_score}, "
                      f"Player Two {self.p2_score}")

            elif self.p2.beats(move2, move1):  # or is True
                print("** PLAYER TWO WINS **")
                # print(f"This Round : Player 2 WIN")
                self.p2_score += 1
                print(f"Score: Player One {self.p1_score}, "
                      f"Player Two {self.p2_score}")

            else:
                print("** TIE **")
                print(f"Score: Player One {self.p1_score}, "
                      f"Player Two {self.p2_score}")

    # Game start point!
    def play_game(self):
        # print("Game start!")
        print("Rock Paper Scissors, Go!")
        for round in range(8):
            print(f"\nRound {round} --")
            self.play_round()
        # print("Game over!")

        # Last required thing: At the end of the game, have it print out which
        # player won, and what the final scores are.
        if self.p1_score > self.p2_score:
            print("\nPlayer 1 is the winner ^_^")
        elif self.p1_score < self.p2_score:
            print("Player 2 is the winner ^_^")
        else:
            print("Its Tie >_<")
        print(f"Final score: Player One {self.p1_score}, "
              f"Player Two {self.p2_score}")


# Main
if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()


# pycodestyle RPS.py 100% done!
# End! clone on May 10, 2020
