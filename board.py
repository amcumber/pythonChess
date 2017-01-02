###Board###
from header import *

class Board(Chess_Abstract):
    'The chess board'
    #TODO Add location to hold pieces
    def constructBoard():
        border      = "+-----+-----+-----+-----+-----+-----+-----+-----+"
        columnLabel = "   A     B     C     D     E     F     G     H"
        squares     = ["  ", "--", " | "]
        horizPadding= "\t"
        vertPadding = "\n\n"

        border      = horizPadding + border
        columnLabel = horizPadding + border
        print(vertPadding)
        for i in range(8):
            # print column label
            if i == 1:
                print(columnLabel)
            # print horiz border
            print(border)
            # construct square interior
            for j in range(8):
                # Add first number
                if j == 0:
                    space  = (j-8) + squares[2]
                rem = (i + j) % 2
                # Check if piece is pesent
                if !pieces[i,j]
                space  = space  + squares[rem]
            else
            # TODO find piece and print
            # print vert border
            space  = space  + squares[2]
            # Add second number
            if j == 7:
                space  = space + (j-8)
        # print final boarder and label
        if i == 7:
            print(border)
    print(columnLabel)

class Board_Square(Chess_Abstract):
    'Board Square object to hold pieces'
    # TODO
    def __init__(self, column, row):
        self.column = column
        self.row = row

