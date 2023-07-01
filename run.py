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

def get_valid_input():
    """
    Validates and returns user input for coordinates
    """
    while True:
        try:
            x = int(input("Enter the row: "))
            y = int(input("Enter the column: "))
            if x in range(5) and y in range(5):
                return x, y
            else:
                print("Invalid input! Please enter values within the range (0-4).")
        except ValueError:
            print("Invalid input! Please enter valid numbers for row and column.")

def play_game():
    """
    Starts the game
    """
    print("Welcome to Battleship!")
    player_name = input("Please enter your name: ")

    """ 
    Create player and computer objects 
    """

    player = Player(player_name)
    computer = Computer()

    """
    Set up player's ships
    """

    print("\nSet up your ships.")
    for _ in range(player.board.num_ships):
        print("Enter the coordinates for ship {}".format(_ + 1))
        x, y = get_valid_input()
        player.board.add_ship(x, y)

    """
    Set up computers's ships
    """
    print("\nSetting up computer's ships.")
    for _ in range(computer.board.num_ships):
        x = random_point(computer.board.size)
        y = random_point(computer.board.size)
        computer.board.add_ship(x, y)

    
    game_over = False
    while not game_over:
        print("\nPlayer's turn")
        player.board.print()
        print("Make a guess.")
        x, y = get_valid_input()
        result = player.board.guess