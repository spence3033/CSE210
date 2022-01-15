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
    person1 = input("What is the first player's name? ")

    # create a board
    board = [blank, blank, blank, 
             blank, blank, blank, 
             blank, blank, blank]

    # loop if there isn't a winner or if the game isn't a draw
    no_winner = True
    no_tie = True

    while no_winner == True and no_tie == True:
        for item in board:
            is_draw(board)
            is_winner(board)

        # display the board
        display_board(board)
        # allow the player to make a move
        make_move(person1, board)
        # pick the next player

        pass
    # display the final board

    # show message for winner and thanks for playing
    pass

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
    pass

def is_winner(board):
    ''' return: True if someone won, False if there is no winner '''
    pass

def make_move(player, board):
    ''' Prompts player to select a square to play
        Assigns the player to that board location if it is a legal move
        return: None
    '''
    should_move = True
    while should_move == True:
        move = input('Please choose 1-9 for where you want to place and "X": ')
        if board[move-1] == " ":
            board[move-1] = X
            should_move = False
    pass      

def next_player(current):
    ''' return: x if current is o, otherwise x '''
    pass

# run main if this has been called from the command line
if __name__ == "__main__":
    main()
