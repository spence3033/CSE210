'''
Solo Checkpoint 02
Author: Bro. Hayes
'''
X = "X"
O = "O"
blank = " "


def main():
    ''' Holds the main game loop logic
        Selects a player
        Builds the board
        Loops through Players until a winner is found or game is over
        Displays results to user
        Thanks them for playing
        return: None
    '''
    # assign/get the first player
    player = 1
    # create a board
    board = [blank, blank, blank, 
             blank, blank, blank, 
             blank, blank, blank]

    # loop if there isn't a winner or if the game isn't a draw
    no_winner = True
    no_tie = True

    while no_winner == True and no_tie == True:

        # display the board
        display_board(board)
        # allow the player to make a move
        # pick the next player
        player = make_move(player, board)

        no_winner = not is_winner(board)
        no_tie = not is_draw(board)

    # display the final board
    display_board(board)

    # show message for winner and thanks for playing
    print(f'Congradulations! Game over!')

def create_board():
    ''' Creates a list that holds the spots on the board
        It initializes the positions with the numbers for the person to pick
        return: the board as a list
    '''
    pass

def display_board(board):
    ''' Displays the current board
        return: None
    '''
    for x in range(0, 7, 3):
        print(f'\t{board[x+0]} | {board[x+1]} | {board[x+2]}')
        if x < 6:
            print('\t--+---+--')

    pass

def is_draw(board):
    ''' return: True if board is a draw, False if board is still playable '''
    for item in board:
        if item == ' ':
            return False
    return True

def is_winner(board):
    ''' return: True if someone won, False if there is no winner '''
    list_Xs = []
    list_Os = []
    number = 0
    item = board[0]
    if item == 'X' or item == 'O':
        if board[1] == item and board[2] == item:
            return True
        if board[3] == item and board[6] == item:
            return True
        if board[4] == item and board[8] == item:
            return True
    item = board[1]
    if item == 'X' or item == 'O':
        if board[4] == item and board[7] == item:
            return True
    item = board[2]
    if item == 'X' or item == 'O':
        if board[5] == item and board[8] == item:
            return True
    item = board[3]
    if item == 'X' or item == 'O':
        if board[4] == item and board[5] == item:
            return True
    item = board[6]
    if item == 'X' or item == 'O':
        if board[7] == item and board[8] == item:
            return True
        if board[4] == item and board[2] == item:
            return True
    return False

def make_move(player, board):
    ''' Prompts player to select a square to play
        Assigns the player to that board location if it is a legal move
        return: None
    '''
    should_move = True
    while should_move == True:
        move = int(input('Please choose 1-9 for where you want to place your "X" or "O": '))
        move = move - 1
        if board[move] == " ":
            if player == 1:
                board[move] = X
                should_move = False
            if player == 2:
                board[move] = O
                should_move = False
        else:
            print(f'the board has an "{board[move]}" there. Try again.')
    
    if player == 1:
        return 2
    elif player == 2:
        return 1

# run main if this has been called from the command line
if __name__ == "__main__":
    main()
