from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# print ship_row, ship_col

print 'This ocean has rows 0 - 4 and columns 0 - 4:'
print_board(board)
print 'TRY TO SINK MY SHIP!'

def prompt():        
    guess_row = int(raw_input("Which row?:"))
    guess_col = int(raw_input("Which column?:"))
    
    if guess_row < 0 or guess_row > 4 or guess_col < 0 or guess_col > 4:
        print 'ERROR: row and column guesses must be either 0, 1, 2, 3, or 4'

    if guess_row == ship_row and guess_col == ship_col:
        print 'Congratulations! YOU SANK MY BATTELSHIP!'
        board[guess_row][guess_col] = '!'
        print_board(board)
    else:
        print 'You missed my battleship!'
        board[guess_row][guess_col] = 'x'
        print_board(board)
        prompt()
        
prompt()