#!/bin/python3

import turtle
import math
import random


#some globals, since we're not using classes
players = None
first_player = None
game_board = None
turn = None
game_is_playing = False

O_moves = {
        1: (-100, 55),
        2: (0, 55),
        3: (100, 55),
        4: (-100, -45),
        5: (0, -45),
        6: (100, -45),
        7: (-100, -145),
        8: (0, -145),
        9: (100, -145)
    }

X_moves = {
    1: (-150, 150, -50, 150),
    2: (-50, 150, 50, 150),
    3: (50, 150, 150, 150),
    4: (-150, 50, -50, 50),
    5: (-50, 50, 50, 50),
    6: (50, 50, 150, 50),
    7: (-150, -50, -50, -50),
    8: (-50, -50, 50, -50),
    9: (50, -50, 150, -50)
}

# Setup and make new game window
turtle.setup(900, 900)
turtle.mode('standard')
window = turtle.Screen()


#Make TaylorTurtle Instance
taylor = turtle.Turtle()

#Set Cursor shape, width of pen, and drawing speed
taylor.shape('turtle')
taylor.width(5)
taylor.speed(8)


def draw_splash_screen():
    window.clearscreen()
    taylor.penup()
    taylor.goto(-170, 200)
    taylor.setheading(0)
    #'#CE0C24' dk red
    taylor.color('#f08504')
    taylor.write('Welcome to Tic Tac Toe!', font=("Fredericka the Great", 30, "bold"))

    taylor.pendown()
    taylor.goto(-150, 150)
    taylor.pencolor('#4269f5') #dk_blue
    taylor.forward(300)
    taylor.right(90)
    taylor.forward(150)
    taylor.right(90)
    taylor.forward(300)
    taylor.right(90)
    taylor.forward(150)
    taylor.penup()
    taylor.goto(0, 150)
    taylor.right(180)
    taylor.pendown()
    taylor.forward(150)
    taylor.left(135)
    taylor.penup()
    taylor.forward(35)
    taylor.pendown()
    taylor.pensize(8)
    taylor.color('#f08504')
    taylor.forward(135)
    taylor.penup()
    taylor.goto(0, 150)
    taylor.setheading(90)
    taylor.right(135)
    taylor.forward(40)
    taylor.pendown()
    taylor.forward(135)
    taylor.penup()
    taylor.goto(-75, 15)
    taylor.setheading(0)
    taylor.pendown()
    taylor.circle(55)
    taylor.penup()
    taylor.goto(-125, -45)
    taylor.pensize(5)
    taylor.color('#4269f5')
    taylor.write('Please click X or O to play', font=("Handlee", 24, "bold"))

    window.onclick(player_choose_letter, add=True)


def draw_board():
    global game_is_playing, game_board

    taylor.goto(-150, 150)
    taylor.dot(12)

    # border
    taylor.color('#f08504')  # goldenrod color
    taylor.pendown()

    for number in range(4):
        taylor.forward(300)
        taylor.right(90)

    taylor.penup()

    # Set a New Color for the Coordinate Lines
    taylor.color('#8d024a')  # burgundy

    # Cell dividing Lines
    taylor.setheading(270)
    taylor.goto(-50, 150)
    taylor.pendown()

    taylor.forward(300)
    taylor.penup()

    taylor.goto(50, 150)
    taylor.pendown()
    taylor.forward(300)
    taylor.penup()

    taylor.goto(-150, 50)
    taylor.setheading(0)
    taylor.pendown()
    taylor.forward(300)
    taylor.penup()

    taylor.goto(-150, -50)
    taylor.pendown()
    taylor.forward(300)
    taylor.penup()

    #return to origin
    taylor.goto(-150, 150)

    game_board = [''] * 10
    game_is_playing = True
    play_game()


#writes out mouseclick coordinates for debugging
def log_click(x, y):
    taylor.penup()
    taylor.goto(x, y)
    coordinates = taylor.pos()
    taylor.pendown()
    taylor.pencolor('#000000')
    taylor.write(f'{coordinates}', font=("Handlee", 24))


def draw_play_again():
    #Play again message
    window.clearscreen()
    taylor.penup()
    taylor.goto(0, 50)
    taylor.pendown()
    taylor.color('#000000')
    taylor.write('Play Again??', font=("Fredericka the Great", 40, "bold"), align="center")

    #No arrow (dk red, down)
    taylor.goto(-30, 40)
    taylor.color('#CE0C24')
    taylor.begin_fill()
    taylor.setheading(0)
    taylor.right(120)
    taylor.pendown()
    taylor.forward(50)
    taylor.right(120)
    taylor.forward(50)
    taylor.right(120)
    taylor.forward(50)
    taylor.end_fill()

    #YES arrow (green, up)
    taylor.setheading(0)
    taylor.penup()
    taylor.forward(60)
    taylor.right(60)
    taylor.pendown()
    taylor.begin_fill()
    taylor.color('#78f542') #bright green
    taylor.forward(50)
    taylor.right(120)
    taylor.forward(50)
    taylor.right(120)
    taylor.forward(50)
    taylor.end_fill()

    window.onclick(handle_play_again, add=True)


def handle_play_again(x, y):
    global game_is_playing
    taylor.penup()
    taylor.goto(x, y)

    # the first element is the player, the second is the computer.
    if ((-59 < x < -29) and (-3 < y < 43)):
        window.clearscreen()
        taylor.goto(-170, 200)
        taylor.setheading(0)
        taylor.color('#f08504')
        taylor.write('Thank you for Playing!!', font=("Fredericka the Great", 40, "bold"), align="center")
        game_is_playing = False
        window.ontimer(window.bye, 2000)

    elif ((30 <x < 58) and (-3 < y < 43)):
        window.ontimer(draw_splash_screen, 3000)


def player_choose_letter(x, y):
    #import the globals so they can be updated
    global players

    # Player chooses which letter they want to be.
    # Returns tuple(player's letter,  computer's letter)
    taylor.penup()
    taylor.goto(x, y)
    taylor.right(360)
    x, y = taylor.pos()

    O_first = ('O', 'X')
    X_first = ('X', 'O')

    # the first element is the player, the second is the computer.
    if ((-150 < x < -1) and (1 < y < 150)):
        window.clearscreen()
        taylor.penup()
        taylor.goto(0,0)
        taylor.color('#000000')
        taylor.write(f'Player chooses {O_first[0]}!', font=("Fredericka the Great", 40, "bold"), align="center")
        taylor.goto(0, -40)
        taylor.write(f'Computer will be {O_first[1]}!', font=("Fredericka the Great", 40, "bold"), align="center")

        players = O_first


    elif ((1 <x < 150) and (2 < y < 150)):
        window.clearscreen()
        taylor.penup()
        taylor.goto(0, 20)
        taylor.color('#000000')
        taylor.write(f'Player chooses {X_first[0]}!', font=("Fredericka the Great", 40, "bold"), align="center")
        taylor.goto(0, -40)
        taylor.write(f'Computer will be {X_first[1]}!', font=("Fredericka the Great", 40, "bold"), align="center")

        players = X_first

    window.ontimer(taylor.clear, 1500)
    window.ontimer(set_first_move, 2000)


def set_first_move():
    #import globals so they can be updated
    global players, first_player, turn, game_is_playing

    #Randomly choose the player who goes first.
    first_player = 'Computer' if random.randint(0, 1) == 1 else 'Player'

    #Set the player letter for the turn
    if first_player == 'Computer':
        turn = players[1]
    else:
        turn = players[0]

    #Print first_player to screen
    taylor.penup()
    taylor.goto(0, 170)
    taylor.color('#000000')
    taylor.write(f'{first_player} goes first.', font=("Fredericka the Great", 40, "bold"), align="center")

    #game_is_playing = True
    print('FROM SET PLAYER::  ', turn)

    draw_board()

    return first_player


def draw_x(x1, y1, x2, y2):
    #left diagonal
    taylor.penup()
    taylor.goto(x1, y1)
    taylor.setheading(90)
    taylor.right(135)
    taylor.forward(10)
    taylor.pendown()
    taylor.forward(120)
    taylor.penup()

    #right diagonal
    taylor.penup()
    taylor.goto(x2, y2)
    taylor.setheading(90)
    taylor.left(135)
    taylor.forward(10)
    taylor.pendown()
    taylor.forward(120)
    taylor.penup()


def draw_o(x, y):
    taylor.penup()
    taylor.goto(x, y)
    taylor.setheading(0)
    taylor.pendown()
    taylor.circle(45)
    taylor.penup()


def play_square(x, y):
    global game_board, turn, O_moves, X_moves

    print(x, y)

    if ((-150 < x < -50) and (50 < y < 150)):
        draw_x(*X_moves[1]) if turn == 'X' else draw_o(*O_moves[1])
        game_board[1] = turn
        if turn == players[1]:
            turn = players[0]
        else:
            turn = players[1]

    if ((-51 < x < 50) and (50 < y < 150)):
        draw_x(*X_moves[2]) if turn == 'X' else draw_o(*O_moves[2])
        game_board[2] = turn
        if turn == players[1]:
            turn = players[0]
        else:
            turn = players[1]

    if ((51 < x < 150) and (50 < y < 150)):
        draw_x(*X_moves[3]) if turn == 'X' else draw_o(*O_moves[3])
        game_board[3] = turn

        if turn == players[1]:
            turn = players[0]
        else:
            turn = players[1]

    if ((-150 < x < -50) and (-50 < y < 51)):
        draw_x(*X_moves[4]) if turn == 'X' else draw_o(*O_moves[4])
        game_board[4] = turn

        if turn == players[1]:
            turn = players[0]
        else:
            turn = players[1]

    if ((-51 < x < 50) and (-50 < y < 51)):
        draw_x(*X_moves[5]) if turn == 'X' else draw_o(*O_moves[5])
        game_board[5] = turn
        if turn == players[1]:
            turn = players[0]
        else:
            turn = players[1]

    if ((51 < x < 150) and (-50 < y < 51)):
        draw_x(*X_moves[6]) if turn == 'X' else draw_o(*O_moves[6])
        game_board[6] = turn
        if turn == players[1]:
            turn = players[0]
        else:
            turn = players[1]

    if ((-150 < x < -50) and (-150 < y < -51)):
        draw_x(*X_moves[7]) if turn == 'X' else draw_o(*O_moves[7])
        game_board[7] = turn
        if turn == players[1]:
            turn = players[0]
        else:
            turn = players[1]

    if ((-51 < x < 50) and (-150 < y < -51)):
        draw_x(*X_moves[8]) if turn == 'X' else draw_o(*O_moves[8])
        game_board[8] = turn
        if turn == players[1]:
            turn = players[0]
        else:
            turn = players[1]

    if ((51 < x < 150) and (-150 < y < -51)):
        draw_x(*X_moves[9]) if turn == 'X' else draw_o(*O_moves[9])
        game_board[9] = turn
        if turn == players[1]:
            turn = players[0]
        else:
            turn = players[1]

    print('CURRENT GAME BOARD::  ', game_board)
    print('NEXT TURN::  ', turn)
    return


def space_taken():
    global turn

    taylor.penup()
    taylor.goto(150, -160)
    taylor.pencolor('#000000')
    taylor.write(f'That square\'s been taken already by {turn}', font=("Fredericka the Great", 20, "bold"), align="center")

    window.ontimer(taylor.clear, 1000)


def is_board_full():
    # True if every space is taken.
    for number in range(1, 10):
        if game_board[number] == '':
            return False
    return True


def is_winner(board, player):
    # returns True if player has won.

    letters = [f'{player}', f'{player}', f'{player}']

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


def choose_random_move(moves_list):
    global game_board

    # Returns valid move or None for passed moves_list.
    possible_moves = [item for item in moves_list
                      if game_board[item] == '']

    return random.choice(possible_moves) if possible_moves else None


def get_computer_move():

    # First, check if there is a win in the next move
    for number in range(1, 10):
        copy = game_board[:]
        if game_board[number] == '':
            copy[number] = players[1]

            if is_winner(copy, players[1]):
                return number

    # Then check if *player* can win on their next move & attempt a block.
    for number in range(1, 10):
        copy = game_board[:]
        if game_board[number] == '':
            copy[number] = players[0]
            if is_winner(copy, players[0]):
                return number

    # Try to take one of the corners.
    move = choose_random_move([1, 3, 7, 9])
    if move is not None:
        return move

    # Try to take the center.
    if game_board[5] == '':
        return 5

    # Try one of the sides.
    return choose_random_move([2, 4, 6, 8])


def play_game():
    global game_is_playing

    print(game_board)
    print(players)
    print(turn)
    print(game_is_playing)
    window.onclick(play_square)


    while game_is_playing:
        if turn == players[0]:
            window.update()
            if is_winner(game_board, players[0]):
                window.clearscreen()
                taylor.goto(0, 0)
                taylor.color('#f08504')
                taylor.write("You've beaten the Computer.  YAY!!", font=("Fredericka the Great", 40, "bold"),
                             align="center")
                game_is_playing = False
                window.ontimer(draw_play_again, 2000)
                break
            else:
                if is_board_full():
                        window.clearscreen()
                        taylor.goto(0, 0)
                        taylor.color('#f08504')
                        taylor.write('The game is a tie!', font=("Fredericka the Great", 40, "bold"),
                                     align="center")
                        game_is_playing = False
                        window.ontimer(draw_play_again, 2000)
                        break

        if turn == players[1]:
            print('CURRENT PLAYER IS COMPUTER')
            move = get_computer_move()
            play_square(*O_moves[move])
            print('COMPUTER IS MOVING:: ', players[1])
            window.update()

            if is_winner(game_board, players[1]):
                window.clearscreen()
                taylor.goto(0, 0)
                taylor.color('#f08504')
                taylor.write('The computer has beaten you! \nYou lose. Sad Times.',
                             font=("Fredericka the Great", 40, "bold"),
                             align="center")
                game_is_playing = False
                window.ontimer(draw_play_again, 2000)
                break

            else:
                if is_board_full():
                    window.clearscreen()
                    taylor.goto(0, 0)
                    taylor.color('#f08504')
                    taylor.write('The game is a tie!', font=("Fredericka the Great", 40, "bold"),
                                 align="center")
                    game_is_playing = False
                    window.ontimer(draw_play_again, 2000)
                    break


draw_splash_screen()
window.mainloop()