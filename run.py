from random import randint
from colorama import Fore


scores = {"computer": 0, "player": 0}


class Board:
    """
    Creates the game board
    """
    def __init__(self, size):
        self.size = size
        self.board = [["." for _ in range(size)] for _ in range(size)]
        self.num_ships = 0
        self.name = ""
        self.type = ""
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
        if (x, y) in self.ships:
            self.board[x][y] = "@"
            self.ships.remove((x, y))
            return "Hit"
        else:
            self.board[x][y] = "*"
            return "Missed"

    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print(Fore.RED + "Error: You cannot add any more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "$"


def random_point(size):
    """
    Returning a random integer
    """
    return randint(0, size - 1)


class Player:
    """
    Represents a player in the game
    """
    def __init__(self, name):
        self.name = name
        self.board = Board(5)
        self.board.name = self.name
        self.board.type = "player"
        self.board.num_ships = 3


class Computer:
    """
    Represents the computer opponent in the game
    """
    def __init__(self):
        self.name = "Computer"
        self.board = Board(5)
        self.board.name = self.name
        self.board.type = "computer"
        self.board.num_ships = 3


def get_valid_input(board, guesses):
    """
    Validates and returns user input for coordinates
    """
    while True:
        try:
            x = int(input(Fore.LIGHTYELLOW_EX + '''Enter the row
            (within the range 0-4): '''))
            y = int(input('''Enter the column
            (within the range 0-4): '''))
            if x in range(5) and y in range(5):
                if (x, y) in guesses:
                    print(Fore.RED + '''You already tried these coordinates
                    before. Please enter new coordinates.''')
                    continue
                else:
                    return x, y
            else:
                print(Fore.RED + '''Invalid input! Please enter values within
                the range (0-4).''')
        except ValueError:
            print(Fore.RED + '''Invalid input!Please enter valid numbers for
            row and column.''')


def play_game():
    """
    Starts the game
    """
    print(Fore.LIGHTGREEN_EX + "Welcome to Battleship!")
    while True:
        player_name = input(Fore.LIGHTYELLOW_EX + "Please enter your name: ")
        if len(player_name) >= 3:
            break
        else:
            print(Fore.RED + '''Name must be at least 3 characters long.
             Please try again.''')

    player = Player(player_name)
    computer = Computer()

    print("\nSet up your ships, {}.".format(player_name))
    for _ in range(player.board.num_ships):
        print("Enter the coordinates for ship {}".format(_ + 1))
        x, y = get_valid_input(player.board, player.board.guesses)
        player.board.add_ship(x, y)

    """
    Set up computer's ships
    """
    print("\nSetting up computer's ships.")
    for _ in range(computer.board.num_ships):
        x = random_point(computer.board.size)
        y = random_point(computer.board.size)
        computer.board.add_ship(x, y)

    player_guesses = set()
    computer_guesses = set()

    game_over = False
    while not game_over:
        print("\n{}'s board".format(player_name))
        player.board.print()
        print("Computer's board:")
        computer.board.print()
        print("Make a guess.")
        x, y = get_valid_input(player.board, player_guesses)
        player_guesses.add((x, y))
        result = computer.board.guess(x, y)
        print(result)

        if result == "Hit":
            if len(computer.board.ships) == 0:
                print(Fore.GREEN + '''Congratulations, {}! You sank all the
                computer's ships. You win!'''.format(player_name))
                scores["player"] += 1
                game_over = True
        else:
            print("{} missed.".format(player_name))

        print("\nComputer's turn")
        valid_guess = False
        while not valid_guess:
            x = random_point(player.board.size)
            y = random_point(player.board.size)
            if (x, y) not in computer_guesses:
                valid_guess = True
        computer_guesses.add((x, y))

        result = player.board.guess(x, y)
        print("The computer guesses ({}, {}).".format(x, y))
        print(result)

        if result == "Hit":
            if len(player.board.ships) == 0:
                print(Fore.RED + '''Oops! The computer sank all your
                ships, {}. You lose!'''.format(player_name))
                scores["computer"] += 1
                game_over = True
        else:
            print("The computer missed.")

    print(Fore.RED + "\nGame Over!")
    print(Fore.MAGENTA + "\n{}'s Score:".format(player_name), scores["player"])
    print("Computer Score:", scores["computer"])
    play_game()


if __name__ == "__main__":
    play_game()
