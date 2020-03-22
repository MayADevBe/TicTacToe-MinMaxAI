from board import Board

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

board = Board("TicTacToe", 100)
board.draw()
board.draw_text("x", 2, 2, "red")
board.draw_text("x", 2, 1, "red")
board.draw_text("x", 2, 0, "red")
check_win()
board.start()