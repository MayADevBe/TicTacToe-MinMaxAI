import tkinter as tk

class Board:
    '''Creates GUI Board'''

    def __init__(self, title, width):
        self.window = tk.Tk()
        self.window.title(title)
        self.width = width
        self.field = []
        self.platform = tk.Canvas(self.window, width = 3*width, height = 3*width)
        self.platform.pack()

    def draw(self):
        for i in range(3):
            self.field.append([])
            for j in range(3):
                self.field[i].append("")
                self.platform.create_rectangle(i*self.width, j*self.width, (i+1)*self.width, (j+1)*self.width, fill="white")
        
    def draw_text(self, text, i, j, color):
        rndfont = 25
        self.field[i][j] = text
        self.platform.create_text((self.width/2)*((i*2)+1), (self.width/2)*((j*2)+1), text=text, font=('Pursia', rndfont) ,anchor="center", fill=color, tags=text)

    def start(self):
        self.window.mainloop()

# board = Board("TicTacToe", 100)
# board.draw()
# board.draw_text("o", 0, 0, "green")
# board.draw_text("x", 1, 1, "red")
# board.draw_text("x", 2, 2, "red")
# print(board.field)
# board.start()