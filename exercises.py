# Your goal is to implement the following user stores:

# As a user (AAU), I want to see a welcome message at the start of a game.

# AAU, before being prompted for a move, I want to see the board printed in the console to know what moves have been made.

# AAU, at the beginning of each turn, told whose turn it is: It’s player X’s turn!

# AAU, I should be prompted to enter a move and be provided an example of valid input ('Enter a valid move (example: A1)').

# AAU, I want to be able to enter my move’s column letter in upper or lower case (a/A, b/B, or c/C) to make it easier to enter my move.

# AAU, if I enter a move in an invalid format or try to occupy a cell already taken, I want to see a message chastising me and be re-prompted.

# AAU, after entering a move, I should once again be presented with the updated game board, notified of the current turn, and asked to enter a move for the other player. This process should continue until there is a winner or a tie

# AAU, I should see a message at the end of the game indicating the winner or stating that the game ended in a tie.



# Step 1:
class Game:
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
        'a1': None, 'b1': None, 'c1': None,
        'a2': None, 'b2': None, 'c2': None,
        'a3': None, 'b3': None, 'c3': None,
        }

# game = Game()
# print(game.turn)      # Output: 'X'
# print(game.tie)       # Output: False
# print(game.winner)    # Output: None
# print(game.board)     # Output: {'a1': None, 'b1': None, 'c1': None, 'a2': None, 'b2': None, 'c2': None, 'a3': None, 'b3': None, 'c3': None}


# Step 2:
    def play_game(self):
        # Printing the Welcome Message
        print('Welcome to Tic-Tac-Toe!')
        self.render()



# Step 3:
    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if self.tie == True:
            print("Tie game!")
        elif self.winner != None:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")



    def render(self):
        self.print_message()
        # self.get_move()
        self.print_board()


# Step 4
    def get_move(self):
        while True:
            move = input(f"Player {self.turn}, enter a valid move (example: A1): ").lower()
            # This checks if the player's input (move) is a valid key in the board dictionary.
            # This checks if the specified position on the board is currently unoccupied.
            if move in self.board and self.board[move] is None:
                # This line updates the game board by placing the current player's mark ('X' or 'O') in the specified position.
                self.board[move] = self.turn
                break
            else:
                print("Invalid move. Please try again with an accepted entry.")




# Instantiate the Game class and invoke the play_game method
game_instance = Game()
game_instance.play_game()