
class Board:
    ROWS = 8
    COLS = 8

    def init_board(self):
       board = []
       for x in range(self.COLS):
           for y in range(self.ROWS):
               board.append("*")

    def print_board(self):
        for x in range(self.COLS):
            print("")
            for y in range(self.ROWS):
                print("* ", end = '')

        
