from random import randint

scores = {"computer": 0, "player" : 0}

class Board:
    """
    Creates the game board
    """
    def create_board(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)] 
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []
    
    def print(self):
        for row in self.board:
            print(" ".join(row))
    
    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x,y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Missed"
    
    def add_ship(self, x, y, type="computer"):
        """
        Adding ships
        """
        if len(self.ships) >= self.num_ships:
            print("Error: You cannot add anymore ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"

def random_point(size):
    """
    Returning a random integer 
    """
    return randint(0, size -1)

class Player:
    """
    Represents a player in the game
    """
    def __init__(self, name):
        self.name = name
        self.board = Board()
        self.board.name = self.name
        self.board.type = "player"


class Computer:
    """
    Represents the computer opponent in the game
    """
    def __init__(self):
        self.name = "Computer"
        self.board = Board()
        self.board.name = self.name
        self.board.type = "computer"
