# Rock Paper Scissors

## Description
The game has two players. In a single round of the game, each Player secretly chooses one of three moves, or "throws" — rock, paper, or scissors. Then, players reveal their progress at the same time. If both players picked the same move, there is no winner. Otherwise, rock beats scissors, paper beats rock, and scissors beat paper.


## Instruction
In the terminal workspace below, you can play a demo of the Rock Paper Scissors game. Try entering different moves: type in rock, paper, or scissors to play a round against a computer player. The game has eight rounds.

In the end of the code you will find this code:

```python
# Main
if __name__ == '__main__':
game = Game(HumanPlayer(), ReflectPlayer())
game.play_game()
```


You have four modes you can choose:


* Set the program to play a game between `HumanPlayer()` and `RandomPlayer()`.
If you want the computer to chose randomly.


* Or set the program to play a game between `HumanPlayer()` and `CyclePlayer()`.
If you want the computer to choose Cycle moves:


The start of the computer cycle will be chosen randomly, by the computer; 
let's say it chooses the 'rock' so it will go like:

```
rock -> paper -> scissors -> rock ...etc
```


* Or set the program to play a game between `HumanPlayer()` and `ReflectPlayer()`. 
This class remembers what move the opponent played last round and plays that move this round. (In other words, if you play 'scissors' on the first round, a ReflectPlayer will play 'scissors' on the next round.)


* Or, If you chose to set the program to play a game between `HumanPlayer()` and `Player()`.
The class will always play 'rock'. That's not a very good playing strategy!


Otherwise, you can use `RandomPlayer()`, `ReflectPlayers()` or `Player()` as the `second argument`, but
__don't__ choose `HumanPlayer()` as the `second argument`.


After you save the file. Run the code by using `python3` make sure you have the updated one if you don't have it install it from [here](https://www.python.org/downloads/?target=_blank)
```shell
$ python3 RPS.py
```
To start playing, 
ENJOY ^_^

