from board import Board
from minmax import TicTacToeAI
from math import floor

W_H = 100
turn = "x"
won = ''

against_ai = False
ai_role = ''


def change_turn():
    global turn
    if turn == 'o':
        turn = 'x'
        print(f"It's player {turn}'s turn.")
    else:
        turn = 'o'
        print(f"It's player {turn}'s turn.")

def check_win():
    global board, won, against_ai, ai_role
    field = board.field 
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] and not field[i][0] == "":
            won = field[i][0]
            print(f"{field[i][0]} wins with column {i+1}!")
        elif field[0][i] == field[1][i] == field[2][i] and not field[0][i] == "":
            won = field[i][0]
            print(f"{field[0][i]} wins with row {i+1}!")
    #diagonals
    if field[0][0] == field[1][1] == field[2][2] and not field[0][0] == "":
        won = field[i][0]
        print(f"{field[0][0]} wins with diagonal!")
    elif field[0][2] == field[1][1] == field[2][0] and not field[2][0] == "":
        won = field[i][0]
        print(f"{field[2][0]} wins with diagonal!")
    
    if won == ai_role and against_ai:
        board.draw_field("red")
    elif not won == "":
        board.draw_field("green")

    draw = True
    for i in range(3):
        for j in range(3):
            if field[i][j] == "":
                draw = False
    if not won == '':
        draw = False
    if draw:
        print("It's a draw!")
        won = 'd'
        board.draw_field("orange")

def make_move(event):
    global W_H, board, turn, ai
    if won == '':
        x = floor(event.x/W_H)
        y = floor(event.y/W_H)
        if board.field[x][y] == "":
            board.field[x][y] = turn
            change_turn()
            board.draw_field("black")
        check_win()
        if against_ai and ai_role==turn and won == "":
            board.field = ai.make_move(board.field)
            change_turn()
            board.draw_field("black")
            check_win()

def start_ai(event = None):
    global against_ai, ai_role, ai, turn
    if not against_ai and won == "":
        print("Starting AI...")
        against_ai = True
        ai_role = turn
        ai = TicTacToeAI(ai_role, 2)
        board.field = ai.make_move(board.field)
        change_turn()
        board.draw_field("black")
        check_win()

def new_game(event=None):
    global board, turn, won, against_ai, ai_role
    if not won == '':
        print("Start New Game")
        board.draw()
        print(board.field)
        turn = "o"
        won = ''

        against_ai = False
        ai_role = ''

board = Board("TicTacToe", W_H)
board.draw()
board.platform.bind("<Button-1>", make_move)
board.platform.bind("<Return>", start_ai)
board.platform.bind("<space>", new_game)
board.platform.focus_set()
board.start()
