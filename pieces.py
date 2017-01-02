# Classes
from header import *
# defines which side the piece is on
# want a board and a prompt to ask player 1 and player 2 to move a piece from
# one spot to a new spot. first need location and desitination then add rules to
# moves. Then add inuitive statements.
# 1.need to print a board
# 2. need to refresh the board after a move is made
# 3. need a player as a class that holds other classes
# 4. need abstract classes as pawn, rook, knight, bishop, queen, king
# 5. need init these classes when a white and and black player begins
# 5. need intuitive call st a pawn at e3 and a call of 'e4' will produce the
#      the desired result
# 6. need a way to determine check mate. (a number of moves left, type thing)
# 7. can implement a look prediction // hint thing

# Minimum releasable product::
# A call to each location to state which piece exists
# a move from a to b
# capture of a at b
# removal of the object
# surendering
#
# # Basic Abstract Class
class ChessPiece(ChessAbstract):
    '''Base Class for a chess peice'''
    __metaclass__ = ABCMeta

    side      = 'undef'
    piece     = 'undef'
    color     = 'undef'
    row       = -1
    column    = 0
    position  = (-1, -1) # column, row eg A1
    value     = -1
    captured  = False
    firstMove = True

    def convCol(self, colLett):
        '''Convert a Column Letter to a number'''
        output = -1
        #TODO not unpacking correct::is unbacking as i :: (i,column)
        #TODO look into
        for i, column in enumerate(self.columnLetts):
            if colLett == column:
                output = i
        return output

    # This sets a column to a column letter
    def getCol(self, humanRead=False):
        # Display Col
        if humanRead:
            return self.columnLetts[self.column]
        else:
            return self.column

    def getRow(self, humanRead=False):
        # Display Row
        if humanRead:
            return self.row + 1
        else:
            return self.row

    def setCol(self, columnLett, humanRead=False):
        # Column from Letter 'A', 'B', etc.
        if humanRead:
            self.column = self.convCol(columnLett)
        # Set Col from number
        else:
            self.column   = columnLett

        self.setPosition()
        return self.column

    def setRow(self, row, humanRead=False):
        # SetRow from Human Readable
        if humanRead:
            self.row = row - 1
        # SetRow from Raw value (0-indexed)
        else:
            self.row = row

        self.setPosition()
        return self.row

    def getPosition(self):
        # Display the position of the piece
        return self.position

    def setPosition(self):
        # Reset the position of the piece
        self.position = (self.column, self.row)

        return self.position

    def getCoords(self, inputVal):
        '''Pull Row and Col from position'''
        colLett = inputVal[0]
        row     = inputVal[1] - 1
        colNum  = self.convCol(colLett)
        return colNum, row

    def calcDiff(self, start, end):
        '''Calc a difference between a and b vectors'''
        startVec   = self.getPosition()
        endVec     = self.convCol(end)
        difference = endVec - startVec
        return difference

    def movePiece(self, end):
        '''Move a piece to a final destination'''
        endVec     = self.convCol(end)
        self.firstMove = False
        self.setCol(endVec[0])
        self.setRow(endVec[1])

        return self.getPosition()

    def __str__(self):
        print('%s%s%s: %s%d' % (self.color,
                                self.side,
                                self.piece,
                                self.getCol(humanRead=True),
                                self.getRow(humanRead=True)
                               )
             )

## Used Classes
class Pawn(ChessPiece):
    '''pawn class'''
    def __init__(self, color='undef',column='undef'):
        self.piece    = 'p'
        self.value    = 1
        # Row
        self.__setRowInit(color)
        # Column
        self.setCol(column)

    def __setRowInit(self, color='undef'):
        # Row
        if   color == 'white':
            self.setRow(1)
        elif color == 'black':
            self.setRow(6)

        return self.row

    def move(self, ending):
        '''pawn Specific Move'''
        difference = self.calcDiff(self.getPosition(),ending)
        err = 0
        if difference[0] == 0:
            if difference[1] == 2 and self.firstMove:
                self.movePiece(ending)
            elif difference[1] == 1:
                self.movePiece(ending)
            else:
                err = 1
        else:
            err = 1
        if err:
            print('Illegal Move, Try Again')
        return self.getPosition()

    def attack(self, ending):
        '''pawn Specific Atck'''
        #TODO en passant
        difference = self.calcDiff(self.getPosition(),ending)
        if abs(difference[0]) == 1 and difference[1] == 1:
            self.movePiece(ending)
        else:
            print('Illegal Move, Try Again')
        return self.getPosition()

class Aristocrat(ChessPiece):
    '''Abstract non-pawn class'''

    def __setRowInit(self, color='undef'):
        # Row
        if   color == 'white':
            self.setRow(0)
        elif color == 'black':
            self.setRow(7)

        return self.row

class Rook(Aristocrat):
    '''rook class'''
    def __init__(self, color='undef',side='undef'):
        self.piece = 'R'
        self.value = 5
        # Row
        self.__setRowInit(color)
        # Column - get q side
        if   side == 'q':
            self.setCol('A', humanRead=True)
        # get k side
        elif side == 'k':
            self.setCol('H', humanRead=True)

    def move(self, ending):
        '''rook Specific Move'''
        difference = self.calcDiff(self.getPosition(),ending)
        if difference[0] == 0 or difference[1] == 0:
            self.movePiece(ending)
        else:
            print('Illegal Move, Try Again')
        return self.getPosition()

    def attack(self, ending):
        self.move(ending)

#     def castle(self, side):

class Knight(Aristocrat):
    '''knight class'''
    def __init__(self, color='undef',side='undef'):
        self.piece = 'N'
        self.value = 3
        # Row
        self.__setRowInit(color)

        # Column
        if   side == 'q':
            self.setCol('B', humanRead=True)
        elif side == 'k':
            self.setCol('G', humanRead=True)

    def move(self, ending):
        #format to [n,m] and must return either T or F
        difference = self.calcDiff(self.getPosition(),ending)
        if (abs(difference[0]) == 1 and abs(difference[1]) == 2) \
            or (abs(difference[0]) == 2 and abs(difference[1]) == 1):
            #Check Attack TODO
            self.movePiece(ending)
        else:
            print('Illegal Move, Try Again')
    #need a way to validate jumping vs walking

    def attack(self, ending):
          self.move(ending)

class Bishop(Aristocrat):
    '''bishop class'''
    def __init__(self, color='undef',side='undef'):
        self.piece = 'B'
        self.value = 3
        # Row
        self.__setRowInit(color)
        # Column
        if   side == 'q':
            self.setCol('C', humanRead=True)
        elif side == 'k':
            self.setCol('F', humanRead=True)

    def move(self, ending):
        #format to [n,m] and must return either T or F
        difference = self.calcDiff(self.getPosition(),ending)
        if abs(difference[0]) == abs(difference[1]):
            #Check Attack TODO
            #CHeck LOS TODO
            self.movePiece(ending)
        else:
            print('Illegal Move, Try Again')

    def attack(self, ending):
          self.move(ending)

class Queen(Aristocrat):
    '''queen class'''
    def __init__(self, color='undef'):
        self.piece  = 'Q'
        self.value  = 9
        # Row
        self.__setRowInit(color)
        # Column
        self.setCol('D', humanRead=True)

    def move(self, ending):
        #format to [n,m] and must return either T or F
        difference = self.calcDiff(self.getPosition(),ending)
        if (abs(difference[0]) == abs(difference[1])) != \
            (difference[0] == 0 != difference[1] == 0):
            #Check Attack TODO
            #CHeck LOS TODO
            self.movePiece(ending)
        else:
            print('Illegal Move, Try Again')

    def attack(self, ending):
          self.move(ending)

class King(Aristocrat):
    '''king class'''
    def __init__(self, color='undef'):
        self.piece  = 'K'
        self.value  = 100
        # Row
        self.__setRowInit(color)
        # Column
        self.setCol('E', humanRead=True)

    def move(self, ending):
        #format to [n,m] and must return either T or F
        difference = self.calcDiff(self.getPosition(),ending)
        if abs(difference[1]) == 1 or abs(difference[0] == 1):
            #Check Attack TODO
            #CHeck LOS TODO
            self.movePiece(ending)
        else:
            print('Illegal Move, Try Again')
    #additional legal moves must be added for kings TODO

    def attack(self, ending):
          self.move(ending)

#     def castle(self, side)
