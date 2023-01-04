import random

import game_styling as gs

LEGAL_MOVES = {'x1': ' ', 'x2': ' ', 'x3': ' ', 'y1': ' ', 'y2': ' ', 'y3': ' ', 'z1': ' ', 'z2': ' ', 'z3': ' '}


def draw_board():
    board = f"""x:   {LEGAL_MOVES['x1']} | {LEGAL_MOVES['x2']} | {LEGAL_MOVES['x3']} 
    -----------
y:   {LEGAL_MOVES['y1']} | {LEGAL_MOVES['y2']} | {LEGAL_MOVES['y3']} 
    -----------
z:   {LEGAL_MOVES['z1']} | {LEGAL_MOVES['z2']} | {LEGAL_MOVES['z3']}
     1   2   3"""
    return board


def start():
    print(gs.title)
    mode = input("\nChoose game mode:\nType '1' for 2 player mode, or '2' to play against AI.\n")
    print(f"Instructions:\nTo choose what section to place your marker, please type in the cell reference as shown "
          f"in the grid below (e.g. 'x2'):\n{gs.board_example}")
    if mode == '1':
        two_player()
    elif mode == '2':
        play_ai()
    else:
        print("Please type choice '1' or '2'.")
        start()


def player_turn(turn, ai):
    if not ai:
        if turn % 2 == 0:
            player = 1
            shape = 'X'
        else:
            player = 2
            shape = 'O'
        print(f"\nPlayer {player} (symbol: '{shape}'):")
        print(draw_board())
        return input("Place marker in cell: ").lower(), shape
    else:
        if turn % 2 == 0:
            player = 1
            shape = 'X'
            print(f"\nPlayer {player} (symbol: '{shape}'):")
            print(draw_board())
            return input("Place marker in cell: ").lower(), shape
        else:
            player = 2
            shape = 'O'
            print(f"\nPlayer {player} (AI) (symbol: '{shape}'):")
            print(draw_board())
            ai_choice = random.choice(free_cell_checker())
            return ai_choice, shape


def legal_move_checks(turn, moves_made, ai):
    move, shape = player_turn(turn, ai)
    if move in LEGAL_MOVES and move not in moves_made:
        moves_made[move] = shape
        LEGAL_MOVES[move] = shape
    elif move not in LEGAL_MOVES:
        print(f"Cell does not exist. Please try again and use a free cell.\nFree cells are: {free_cell_checker()}")
        legal_move_checks(turn, moves_made, ai)
    else:
        print(f"Cell already filled. Please try again and use a free cell.\nFree cells are: {free_cell_checker()}")
        legal_move_checks(turn, moves_made, ai)


def free_cell_checker():
    return [cell for cell, value in LEGAL_MOVES.items() if value == ' ']


def win_checker():
    win_conditions = [['x1', 'x2', 'x3'],
                      ['y1', 'y2', 'y3'],
                      ['z1', 'z2', 'z3'],
                      ['x1', 'y1', 'z1'],
                      ['x2', 'y2', 'z2'],
                      ['x3', 'y3', 'z3'],
                      ['x1', 'y2', 'z3'],
                      ['x3', 'y2', 'z1']]
    for condition in win_conditions:
        coords_list = []
        for coord in condition:
            coords_list.append(LEGAL_MOVES[coord])
        if coords_list.count(coords_list[0]) == 3 and ' ' not in coords_list:
            if coords_list[0] == 'X':
                player = 1
            else:
                player = 2
            return True, player
    return False, None


def two_player():
    ai = False
    moves_made = {}
    for turn in range(9):
        legal_move_checks(turn, moves_made, ai)
        game_finished, player = win_checker()
        if game_finished:
            return print(f"\nPlayer {player} wins!"), print(draw_board())
    return print("\nThe game is a draw."), print(draw_board())


def play_ai():
    ai = True
    moves_made = {}
    for turn in range(9):
        legal_move_checks(turn, moves_made, ai)
        game_finished, player = win_checker()
        if game_finished:
            return print(f"\nPlayer {player} wins!"), print(draw_board())
    return print("\nThe game is a draw."), print(draw_board())


start()
