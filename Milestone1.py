from IPython.display import clear_output
import random

# Display initialized board
def display_board(board):
    clear_output()
    print('|' + board[7] + '|' + board[8] + '|' + board[9] + '|')
    print('|' + board[4] + '|' + board[5] + '|' + board[6] + '|')
    print('|' + board[1] + '|' + board[2] + '|' + board[3] + '|')


# Ask for user input to determine mark type for each player
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        # ask player one to pick a mark
        marker = input('Player 1 choose X or O: ')
    if marker == 'X' or marker == 'O':
        player1 = marker
    else:
        marker = input('Player 1 choose X or O: ')

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    players = {'player1': player1, 'player2': player2}
    players_key = list(players.keys())
    players_val = list(players.values())
    return players,players_key,players_val


# Place mark for current player
def place_marker(board, marker, position):
    board[position] = marker
    return board


# Randomly determine first player
def choose_first():
    return random.randint(1, 2)


# Check avaialbe space on the board
def space_check(board):
    # check if there free space on the board
    if ' ' in board:
        indecies = [i for i, val in enumerate(board) if val == ' ']
        indecies = indecies[1:]
        return True,indecies
    else:
        return False


# Check if players want to replay the game
def replay():
    rc = input('Do you want to replay this game?(Yes/No)')
    if rc == 'Yes':
        return True
    else:
        return False


# Win check
def win_check(board, mark,players_key,players_val):
    if board[1] and board[2] and board[3] == mark:
        winner = players_key[players_val.index(mark)]
        return True, winner
    elif board[1] and board[4] and board[7] == mark:
        winner = players_key[players_val.index(mark)]
        return True, winner
    elif board[1] and board[5] and board[9] == mark:
        winner = players_key[players_val.index(mark)]
        return True, winner
    elif board[2] and board[5] and board[8] == mark:
        winner = players_key[players_val.index(mark)]
        return True, winner
    elif board[3] and board[6] and board[9] == mark:
        winner = players_key[players_val.index(mark)]
        return True, winner
    elif board[4] and board[5] and board[6] == mark:
        winner = players_key[players_val.index(mark)]
        return True, winner
    elif board[7] and board[8] and board[9] == mark:
        winner = players_key[players_val.index(mark)]
        return True, winner
    elif board[3] and board[5] and board[7] == mark:
        winner = players_key[players_val.index(mark)]
        return True, winner
    else:
        winner = 'Game not over'
        return False, winner[0]


# Staring game
def tictactoe():
    print('Welcome to Tic Tac Toe!')

    # check if players want to start playing
    s = input('Do you want to start the game?(Yes/No) \n')
    #initialize an empty board
    initial_board=[' ']*10
    #display empty board
    display_board(initial_board)

    # check who start first
    if s == 'Yes':
        sp = choose_first()  # starting player check
        print('The starting player is player{}'.format(sp))

        # ask start player to pick a marker and store it in a dictionary
        # players = {'player1':player1,'player2':player2}
        player_marks,players_key,players_val = player_input()

        # Initial space check and win check values
        sc = True  # There are always free spaces on the board at the begining
        wc = False  # Game can not be won at the begining

        while sc == True and wc == False:
            # start the game
            mt = input("Please specify current player's marker shape X or O: ")
            if mt == 'X' or mt == 'O':
                pass
            else:
                mt = input("Please specify current player's marker shape X or O: ")

            ml = int(input('Please specify the location you want to put your marker: '))
            # place current player's move onto the board
            current_board = place_marker(initial_board, mt, ml)
            initial_board = current_board
            # space check
            sc,indecies = space_check(current_board)
            print('Avaialbe space is {}'.format(indecies))#show free spaces on the board
            # win check
            print(players_key)
            print(players_val)
            print(mt)
            wc, wp = win_check(current_board, mt,players_key,players_val)
            print(wc)
            print(wp)
            # refresh the board
            display_board(current_board)
            print(current_board[1:])

            # if no space on the board but no one wins, print draw
            if sc == False and wc == False:
                print('No more free space on the board and it is a draw')

            # if anyone wins, print the winner
            elif wc == True:
                print('{} is the winner'.format(wp))

        # Check for replay option
        rc = replay()
        if rc == True:
            tictactoe()
        else:
            print('The game is end')

    else:
        print('Game ended')

# Main
tictactoe()