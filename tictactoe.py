from board import Board
from math import floor

W_H = 100
turn = "o"

def check_win():
    global board
    field = board.field
    for i in range(2):
        #rows
        if field[i][0] == field[i][1] == field[i][2] and not field[i][0] == "":
            print(f"{field[i][0]} wins!")
        #columns
        elif field[0][i] == field[1][i] == field[2][i] and not field[0][i] == "":
            print(f"{field[0][i]} wins!")
    #diagonals
    if field[0][0] == field[1][1] == field[2][2] and not field[0][0] == "":
        print(f"{field[0][0]} wins!")
    elif field[0][2] == field[1][1] == field[2][0] and not field[2][0] == "":
        print(f"{field[2][0]} wins!")
    
    draw = True
    for i in range(2):
        for j in range(2):
            if field[i][j] == "":
                draw = False
    
    if draw == True:
        print("It's a draw!")

def make_move(event):
    global W_H, board, turn
    x = floor(event.x/W_H)
    y = floor(event.y/W_H)
    if board.field[x][y] == "":
        board.draw_text(turn, x, y, "black")
        if turn == 'o':
            turn = 'x'
            print(f"It's player {turn}s turn.")
        else:
            turn = 'o'
            print(f"It's player {turn}s turn.")
    check_win()

board = Board("TicTacToe", W_H)
board.draw()
board.platform.bind("<Button-1>", make_move)
board.platform.focus_set()
board.start()