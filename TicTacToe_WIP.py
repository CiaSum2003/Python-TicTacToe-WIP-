"""
EZ tic-tac-toe game using classes! 

make board, make player affect board, determine win, play again
"""
import random

class TicTacToe:
    def __init__(self):
        self.board = []
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append("-")
                self.board.append(row)
    def who_is_x(self):
        first_player = random.randint(0,1)
        



    # 727