#!/bin/python3
"""
Created on Mon Apr  9 23:20:54 2018
@author: bethanygarcia
"""
import random


def draw_board(board):
    # "board" is a list of 10 strings representing the board (index 0 is empty)

    print(f'-1---2---3--')
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print(f'-4---5---6--')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print(f'-7---8---9--')
    print(f' {board[7]} | {board[8]} | {board[9]}')


def player_input_letter():
    # Player types which letter they want to be.
    # Returns tuple(player's letter,  computer's letter)
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = input('Hi there!\nDo you want to be X or O?\n').upper()

    # the first element is the player, the second is the computer.
    return ('X', 'O') if letter == 'X' else ('O', 'X')


def first_move():
    # Randomly choose the player who goes first.
    return 'computer' if random.randint(0, 1) == 0 else 'player'


def play_again():
    # True if the player wants to play again, otherwise False.
    return input('Do you want to play again? (yes or no)\n')\
                .lower()\
                .startswith('y')

def make_move(board, letter, move):
    board[move] = letter

def is_winner(board, letter):
    # returns True if player has won.

    letters = [f'{letter}', f'{letter}', f'{letter}']

    return (
        # across the bottom: 7, 8, & 9
        board[7:] == letters

        # across the middle: 4, 5 & 6
        or board[4:7] == letters

        # across the top: 1, 2, & 3
        or board[1:4] == letters

        # down the left side: 1, 4 & 7
        or board[1::3] == letters

        # down the middle : 2, 5 ,& 8
        or board[2::3] == letters

        # down the right side : 3, 6, & 9
        or board[3::3] == letters

        # diagonal:  3, 5, & 7
        or board[3:8:2] == letters

        # diagonal: 1, 5, & 9
        or board[1::4] == letters
    )

def is_space_free(board, move):
    # True if passed move is free on passed board.
    return board[move] == ' '

def get_player_move(board):
    # Let the player type in their move.
    move = ' '
    moves = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
    while move not in moves or not is_space_free(board, int(move)):
        move = input('What is your next move? (1-9)\n')
    return int(move)

def choose_random_move(board, moves_list):
    # Returns valid move or None for passed board.
    possible_moves = [item for item in moves_list
                      if is_space_free(board, item)]

    return random.choice(possible_moves) if possible_moves else None


def get_computer_move(board, players):
    # Algorithm Tic Tac Toe:
    # First, check if there is a win in the next move
    for number in range(1, 10):
        copy = board[:]
        if is_space_free(copy, number):
            make_move(copy, players[1], number)
            if is_winner(copy, players[1]):
                return number

    # Then check if *player* can win on their next move & attempt a block.
    for number in range(1, 10):
        copy = board[:]
        if is_space_free(copy, number):
            make_move(copy, players[0], number)
            if is_winner(copy, players[0]):
                return number

    # Try to take one of the corners.
    move = choose_random_move(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center.
    if is_space_free(board, 5):
        return 5

    # Try one of the sides.
    return choose_random_move(board, [2, 4, 6, 8])

def is_board_full(board):
    # True if every space is taken.
    for number in range(1, 10):
        if is_space_free(board, number):
            return False
    return True


print('Welcome to TicTacToe!')

#Main Game Loop

while True:
    # Reset the board
    game_board = [' '] * 10
    players = player_input_letter()
    turn = first_move()
    print(f'The {turn} will go first.')
    game_is_playing = True

    #play loop
    while game_is_playing:
        if turn == 'player':
            draw_board(game_board)
            move = get_player_move(game_board)
            make_move(game_board, players[0], move)

            if is_winner(game_board, players[0]):
                draw_board(game_board)
                print('Hooray! You have won the game!')
                game_is_playing = False
            else:
                if is_board_full(game_board):
                    draw_board(game_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            move = get_computer_move(game_board, players)
            make_move(game_board, players[1], move)

            if is_winner(game_board, players[1]):
                draw_board(game_board)
                print('The computer has beaten you! You lose.')
                game_is_playing = False
            else:
                if is_board_full(game_board):
                    draw_board(game_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    #If player answers "no" they do not want to play again
    if not play_again():
        print('Thank you for playing!')
        break