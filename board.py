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
        self.field = []
        for i in range(3):
            self.field.append([])
            for j in range(3):
                self.field[i].append("")
                self.platform.create_rectangle(i*self.width, j*self.width, (i+1)*self.width, (j+1)*self.width, fill="white")

    def draw_field(self, color):
        rndfont = 25
        for i in range(3):
            for j in range(3):
                if not (self.field[i][j] == ""):
                    self.platform.create_text((self.width/2)*((i*2)+1), (self.width/2)*((j*2)+1), text=self.field[i][j], font=('Pursia', rndfont) ,anchor="center", fill=color, tag=self.field[i][j])

    def start(self):
        self.window.mainloop()