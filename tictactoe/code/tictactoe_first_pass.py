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
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element is the player, the second is the computer.
    if letter == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def first_move():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def play_again():
    # True if the player wants to play again, otherwise False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def make_move(board, letter, move):
    board[move] = letter

def is_winner(board, letter):
    # returns True if player has won.
    return (
        # across the bottom: 7, 8, & 9
        (board[7] == letter and board[8] == letter and board[9] == letter)

        # across the middle: 4, 5 & 6
        or (board[4] == letter and board[5] == letter and board[6] == letter)

        # across the top: 1, 2, & 3
        or (board[1] == letter and board[2] == letter and board[3] == letter)

        # down the left side: 1, 4 & 7
        or (board[7] == letter and board[4] == letter and board[1] == letter)

        # down the middle : 2, 5 ,& 8
        or (board[8] == letter and board[5] == letter and board[2] == letter)

        # down the right side : 3, 6, & 9
        or (board[9] == letter and board[6] == letter and board[3] == letter)

        # diagonal:  3, 5, & 7
        or (board[7] == letter and board[5] == letter and board[3] == letter)

        # diagonal: 1, 5, & 9
        or (board[9] == letter and board[5] == letter and board[1] == letter)
    )

def board_copy(board):
    # return a duplicate of the board
    duplicate_board = []

    for item in board:
        duplicate_board.append(item)

    return duplicate_board

def is_space_free(board, move):
    # True if passed move is free on passed board.
    return board[move] == ' '

def get_player_move(board):
    # Let the player type in their move.
    move = ' '
    moves = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
    while move not in moves or not is_space_free(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def choose_random_move(board, moves_list):
    # Returns valid move or None for passed board.
    possible_moves = []
    for item in moves_list:
        if is_space_free(board, item):
            possible_moves.append(item)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None

def get_computer_move(board, computer_letter):
    # Given a board & the computer's letter, determine move.
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # Algorithm Tic Tac Toe:
    # First, check if there is a win in the next move
    for number in range(1, 10):
        copy = board_copy(board)
        if is_space_free(copy, number):
            make_move(copy, computer_letter, number)
            if is_winner(copy, computer_letter):
                return number

    # Then check if *player* can win on their next move & attempt a block.
    for number in range(1, 10):
        copy = board_copy(board)
        if is_space_free(copy, number):
            make_move(copy, player_letter, number)
            if is_winner(copy, player_letter):
                return number

    # Try to take one of the corners.
    move = choose_random_move(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center.
    if isSpaceFree(board, 5):
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
    player_letter, computer_letter = player_input_letter()
    turn = first_move()
    print(f'The {turn} will go first.')
    game_is_playing = True

    #play loop
    while game_is_playing:
        if turn == 'player':
            draw_board(game_board)
            move = get_player_move(game_board)
            make_move(game_board, player_letter, move)

            if is_winner(game_board, player_letter):
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
            move = get_computer_move(game_board, computer_letter)
            make_move(game_board, computer_letter, move)

            if is_winner(game_board, computer_letter):
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