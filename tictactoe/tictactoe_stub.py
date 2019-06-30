#!/bin/python3
"""
Created on Mon Apr  9 23:20:54 2018
@author: bethanygarcia
"""


def draw_board(board):
    # "board" is a list of 10 strings representing the board (index 0 is empty)
    pass

def player_input_letter():
    # Player types which letter they want to be.
    # Returns tuple(player's letter,  computer's letter)
    pass

def first_move():
    # Randomly choose the player who goes first.
    pass

def play_again():
    # True if the player wants to play again, otherwise False.
    pass

def make_move(board, letter, move):
    pass

def is_winner(board, letter):
    # returns True if player has won.
    return (
        # across the bottom: 7, 8, & 9

        # across the middle: 4, 5 & 6

        # across the top: 1, 2, & 3

        # down the left side: 1, 4 & 7

        # down the middle : 2, 5 ,& 8

        # down the right side : 3, 6, & 9

        # diagonal:  3, 5, & 7

        # diagonal: 1, 5, & 9

    )

def board_copy(board):
    # return a duplicate of the board
    pass


def is_space_free(board, move):
    # True if passed move is free on passed board.
    pass

def get_player_move(board):
    # Let the player type in their move.
    pass

def choose_random_move(board, moves_list):
    # Returns valid move or None for passed board.
    pass

def get_computer_move(board, computer_letter):
    # Given a board & the computer's letter, determine move.
    pass

    # Algorithm Tic Tac Toe:
    # First, check if there is a win in the next move
    pass

    # Then check if *player* can win on their next move & attempt a block.
    pass

    # Try to take one of the corners.
    pass

    # Try to take the center.
    pass

    # Try one of the sides.
    pass

def is_board_full(board):
    # True if every space is taken.
    pass

print('Welcome to TicTacToe!')

#Main Game Loop

while True:
    # Reset board to start play
    pass

    #play loop
    while game_is_playing:
        pass

    #If player answers "no" they do not want to play again
    if not play_again():
        print('Thank you for playing!')

        #break out of Main Game Loop and exit.
        break