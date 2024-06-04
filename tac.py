import random

# Pam Qian 2016 Fall CS 112 Python Midterm Project II
# Tic Tac Toe 

def main():
    introduction = intro()
    board = create_grid()
    pretty = printPretty(board)
    player_symbol, ai_symbol = sym()
    full = isFull(board, player_symbol, ai_symbol)


def intro():
    # This function introduces the rules of the game Tic Tac Toe
    print("Halo! Selamat datang di permainan Tic Tac Toe!")
    print("\n")
    print("Aturan: Player 1, represented by X or O, will play against the computer. "
          "The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins.")
    print("\n")
    input("Press enter to continue.")
    print("\n")


def create_grid():
    # This function creates a blank playboard
    print("Here is the playboard: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board


def sym():
    # This function decides the player's symbol
    symbol = input("Do you want to be X or O? ")
    if symbol == "X":
        ai_symbol = "O"
        print("The computer will be O.")
    else:
        ai_symbol = "X"
        print("The computer will be X.")
    input("Press enter to continue.")
    print("\n")
    return symbol, ai_symbol


def startGamming(board, player_symbol, ai_symbol, count):
    # This function starts the game.
    if count % 2 == 0:
        player_turn(board, player_symbol)
    else:
        ai_turn(board, ai_symbol)
    return board


def player_turn(board, player_symbol):
    print("Player " + player_symbol + ", it is your turn.")
    row, column = get_player_move(board, player_symbol)
    board[row][column] = player_symbol


def get_player_move(board, symbol):
    while True:
        row = int(input("Pick a row:"
                        "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]: "))
        column = int(input("Pick a column:"
                           "[left column: enter 0, middle column: enter 1, right column enter 2]: "))

        if 0 <= row <= 2 and 0 <= column <= 2:
            if board[row][column] == " ":
                return row, column
            else:
                print("The square you picked is already filled. Pick another one.")
        else:
            print("Out of board. Pick another one.")


def ai_turn(board, ai_symbol):
    print("Computer's turn.")
    row, column = get_ai_move(board)
    board[row][column] = ai_symbol
    print(f"Computer placed {ai_symbol} at ({row}, {column}).")


def get_ai_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty_cells)


def isFull(board, player_symbol, ai_symbol):
    count = 0
    winner = True
    while count < 9 and winner:
        board = startGamming(board, player_symbol, ai_symbol, count)
        pretty = printPretty(board)

        if count >= 4:  # Check for a winner after at least 5 moves
            winner = not isWinner(board, player_symbol, ai_symbol)
        count += 1

    if not winner:
        print("Game over.")
    else:
        print("The board is full. Game over. There is a tie.")


def printPretty(board):
    # This function prints the board nice!
    rows = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board


def isWinner(board, player_symbol, ai_symbol):
    # This function checks if there is a winner
    for symbol in [player_symbol, ai_symbol]:
        # Check rows and columns
        for i in range(3):
            if all([cell == symbol for cell in board[i]]) or all([board[j][i] == symbol for j in range(3)]):
                print(f"Player {symbol} wins!")
                return True

        # Check diagonals
        if (board[0][0] == board[1][1] == board[2][2] == symbol) or (board[0][2] == board[1][1] == board[2][0] == symbol):
            print(f"Player {symbol} wins!")
            return True
    return False


# Call Main
main()
