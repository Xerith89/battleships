
class Board:
    ROWS = ['A','B','C','D','E','F','G','H']
    COLS = ['1','2','3','4','5','6','7','8']
    board = list()

    def init_board(self):
       for x in self.COLS:
           position = 0
           for _y in range(8):
               self.board.append(self.ROWS[position] + x)
               position+=1
               

    def print_board(self):
        characters = 0
        print(self.board[8])
        for x in self.board:
            if characters < 7:
                print(x + ' ',end='')
                characters+=1
            else:
                print(x)
                characters = 0
           
        
