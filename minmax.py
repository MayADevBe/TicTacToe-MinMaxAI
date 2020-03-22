class TicTacToeAI:
    '''MinMax Algorithm for Tic Tac Toe'''

    def __init__(self, role, depth):
        self.role = role
        self.depth = depth
        self.next_move = None

    def full_field(self, move):
        full = True
        for i in range(3):
            for j in range(3):
                if move[i][j] == "":
                    full = False
        return full

    def valuation(self, field): # just for winning
        for i in range(3):
            #rows
            if field[i][0] == field[i][1] == field[i][2] and not field[i][0] == "":
                if field[i][0] == self.role:
                    return 1
                else:
                    return -1
            #columns
            elif field[0][i] == field[1][i] == field[2][i] and not field[0][i] == "":
                if field[0][i] == self.role:
                    return 1
                else:
                    return -1
        #diagonals
        if field[0][0] == field[1][1] == field[2][2] and not field[0][0] == "":
            if field[0][0] == self.role:
                return 1
            else:
                return -1
        elif field[0][2] == field[1][1] == field[2][0] and not field[2][0] == "":
            if field[2][0] == self.role:
                return 1
            else:
                return -1   
        return 0  

    def get_possible_moves(self, move, max_player):
        possible_moves = []
        for i in range(3):
            for j in range(3):
                if move[i][j] == "": #possible move
                    new_field = copy_field(move)
                    if max_player:
                        new_field[i][j] = self.role
                    else:
                        if self.role == 'x':
                            new_field[i][j] = 'o'
                        else:
                            new_field[i][j] = 'x'
                    possible_moves.append(new_field)
        if self.next_move == None:
            self.next_move = copy_field(possible_moves[0])
        return possible_moves

    def minmax(self, curr, depth, max_player):
        if depth == 0 or self.full_field(curr):
            return self.valuation(curr)
        if max_player:
            value = -2 # -infinity
            for move in self.get_possible_moves(curr, max_player):
                new_value = self.minmax(move, depth -1, False)
                if new_value > value:
                    value = new_value
                    if depth == self.depth: #store best next move
                        self.next_move = copy_field(move) 
            return value
        else:
            value = 2 # +infinity
            for move in self.get_possible_moves(curr, max_player):
               new_value = self.minmax(move, depth -1, True)
               if new_value < value:
                   value = new_value
            return value

    def make_move(self, field):
        self.next_move = None
        self.minmax(field, self.depth, True)
        return self.next_move

def copy_field(field):
    new_field = []
    for i in range(3):
        new_field.append([])
        for j in range(3):
            new_field[i].append(field[i][j])
    return new_field