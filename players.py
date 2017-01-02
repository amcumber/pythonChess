###Plyers###

from header import *
from pieces import *

class Player(ChessAbstract):
    '''Base class for black and white players'''
    yourMove = False
    def __init__(self, color):
        self.color         =  color
        # Move init
        if self.color      == 'white':
            yourMove       =  True

        sides = ['q','k']

        # Monarchy
        self.queens[0]      = Queen(self.color)
        self.kings[0]       = King(self.color)

        # Arisocrats
        for i, side in enumerate(sides):
            self.rooks[i]   = Rook(self.color,   side)
            self.knights[i] = Knight(self.color, side)
            self.bishops[i] = Bishop(self.color, side)

        # Plebs
        columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for i, column in enumerate(columns):
            self.pawns[i]   = Pawn(self.color,   column)

        # Organize
        self.pieces = {'queen'  : self.queens,
                       'king'   : self.kings,
                       'rooks'  : self.rooks,
                       'knights': self.knights,
                       'bishops': self.bishops,
                       'pawns'  : self.pawns
              }
        self.points = 0

    # Castle, restrictions, en passant
    def move(location, destination):
        '''Move a piece from a location to a destination'''
        # Location needs to look for piece, if exists move it to destination
        pieceFound = False
        pieceIQ    = Pawn('light urple', 'W')                                   # bogus class
        for key, type in self.pieces:
            for piece in type:
                if piece.loc   == location:
                    pieceFound = True
                    pieceIQ    = piece
                    break
                # else:
                    #keep looping TODO
        if pieceFound:
            pieceIQ.move(destination)
            yourMove = False
        else:
            print('Cannot find material, try again')
            #loop! TODO




###########################################################
# Functions
###########################################################

def move_piece(starting, ending):

    starting_num = [int(starting[1]), column_numconverter(starting[0])]
    ending_num = [int(ending[1]), column_numconverter(ending[0])]

    board_start = board[starting_num[0] - 1][starting_num[1] - 1]
    board_end =  board[starting_num[0] - 1][ending_num[1] - 1]
    if board_end == 'o' and board_start != 'o':
        capture = False
        if board_start.moveset(starting_num, ending_num):
            #need to define movesets
            is_legal = True
        else:
            is_legal = False
    elif board_end != 'o' and board_end[0] != board_start[0]
        #this is wrong somehow
        capture = True
        if board_start.attackset(starting_num, ending_num):
            #need to define movesets
            is_legal = True
        else:
            is_legal = False
    else:
        is_legal = False

    if is_legal and not capture:
        board_end = board_start
        board_end.columnname = ending[0]
        board_end.row = ending[1]
        board_start = 'o'
        return True
    elif is_legal and capture:
        scorecard(board_end)
        #write this function to add a score for a capture
        board_end = board_start
        board_end.columnname = ending[0]
        board_end.row = ending[1]
        board_start = 'o'
        return True
    else:
        print "That move is not allowed, try again!"
        #add a repeat of procedure
        return False

