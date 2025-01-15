#Tic tac Toe
#Hayden Lakey
#04 March 2022
import math
import random

class Player:
    def init (self, letter):
        
        self.letter = letter
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def init (self, letter):
        super(). init (letter)
        
    def get_move(self, game):
        square =random.cjoice(game.available_moves())
        return square
    
class HumanPlayer(Player):
    def init (self, letter):
        super(). init (letter)
        
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid Square try again")
        return val