
#defines which side the piece is on
class player(object):
  'Base class for black and white players'
  #TODO

class board(object):
  'The chess board'
  #TODO Add location to hold pieces
  def printBoard():
    border      = "  +----+----+----+----+----+----+----+----+  "
    columnLabel = "    AA   BB   CC   DD   EE   FF   GG   HH    "
    squares     = ["  ", "--", " | "]
    horizPadding= "\t"
    vertPadding = "\n\n"

    border      = horizPadding + border
    columnLabel = horizPadding + border
    print vertPadding
    for i in range(8):
      # print column label
      if i == 1:
        print columnLabel
      # print horiz border
      print border
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
        print border
        print columnLabel

class boardSquare(object):
  'Board Square object to hold pieces'
  # TODO
  def __init__(self, column, row):
    self.column = column
    self.row = row

class chessPiece(object):
  'Base Class for a chess peice'
  capturedFlag = False
  row    = -1
  column = -1
  value  = -1
  piece  = 'undef'
  side   = 'undef'
  firstMove = False
  def moveset(self, starting, ending):
    return False
  def attackset(self, starting, ending):
    return False
  def captured(self,opponent):
    self.capturedFlag = True
    opponent.score += value
  __columnArr = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H'
  ]

  def __str__(self):
    if self.column > -1:
      return '%s%s%s: %s%d' % (self.color, self.side, self.piece, \
        __columnArr(self.column), self.row)
    else:
      return 'UNDEF'
  #def __move__..
  #def __atk__.. (see __add__)
  #def __repr__(self):
  # return (%d) % (self.color)

#defines which side the piece is on
class color(object):
  'Base color for a chess peice'
  color = 'undef'
  row   = -1

class black(color):
  'Base color: Black'
  color = 'b'
  row   = 8

class white(color):
  'Base color: White'
  color = 'w'
  row   = 1

class pawn(chessPiece):
  'Pawn class'
  def __init__(self, color = 'undef'):
    if str(color) == 'w':
      self.row = 2
    elif str(color) == 'b':
      self.row = 7
    else
      self.row = -1
  piece    = 'p'
  value    = 1
  moveset  = (0, 1)
  atackset = (1, 1) or (-1, 1)

  def __str__(self):
    if self.column > -1:
      return '%s%d' % (__columnArr(self.column), self.row)
    else:
      return 'UNDEF'

class rook(chessPiece):
  'Rook class'
  piece = 'R'
  value = 5
  def moveset(self, starting, ending):
    #format to [n,m] and must return either T or F
    differece = starting - ending
    if differece[0] == 0 or differece[1] == 0:
      return True
      firstMove = True
    else:
      return False

  def atackset(self, starting, ending):
      self.moveset(starting, ending)

  def castle(self, side)
    if self.side == False:
      if str(side) == '0-0-0':
       self.column = 3
        return True
        firstMove = True
      elif str(side) == '0-0':
        self.column = 5
        return True
        firstMove = True
      else:
        return False
    else:
      return False

class knight(chessPiece):
  'Knight class'
  piece = 'N'
  value = 3
  def moveset(self, starting, ending):
    #format to [n,m] and must return either T or F
    differece = starting - ending
    if (abs(differece[0]) == 1 and abs(differece[1]) == 2) \
      or (abs(difference[0]) == 2 and abs(differece[1]) == 1):
      return True
    else:
      return False
  #need a way to validate jumping vs walking
  def atackset(self, starting, ending):
      self.moveset(starting, ending)

class bishop(chessPiece):
  'Bishop class'
  piece = 'B'
  value = 3
  def moveset(self, starting, ending):
    #format to [n,m] and must return either T or F
    differece = starting - ending
    if abs(differece[0]) == abs(differece[1]):
      return True
    else:
      return False

  def atackset(self, starting, ending):
      self.moveset(starting, ending)

class queen(chessPiece):
  'Queen class'
  piece  = 'Q'
  value  = 9
  column = 3

  def moveset(self, starting, ending):
    #format to [n,m] and must return either T or F
    differece = starting - ending
    if (abs(differece[0]) == abs(differece[1])) != \
      (differece[0] == 0 != differece[1] == 0):
      return True
    else:
      return False

  def atackset(self, starting, ending):
      self.moveset(starting, ending)

  def __str__(self):
    if self.column > -1:
      return '%s%s: %s%d' % (self.color, self.piece, \
        __columnArr(self.column), self.row)
    else:
      return 'UNDEF'

class king(chessPiece):
  'King class'
  piece  = 'K'
  value  = 100
  column = 4

  def moveset(self, starting, ending):
    #format to [n,m] and must return either T or F
    differece = starting - ending
    if abs(difference[1]) == 1 or abs(difference[0] == 1):
      return True
      self.firstmove = True
    else:
      return False
  #additional legal moves must be added for kings

  def atackset(self, starting, ending):
      self.moveset(starting, ending)

  def castle(self, side)
    if self.side == False:
      if str(side) == '0-0-0':
        self.column = 2
        return True
      elif str(side) == '0-0':
        self.column = 6
        return True
      else:
        return False
    else:
      return False

  def __str__(self):
    if self.column > -1:
      return '%s%s: %s%d' % (self.color, self.piece, \
        __columnArr(self.column), self.row)
    else:
      return 'UNDEF'

###########################################################
# Sides: White
###########################################################

class whitePawn(pawn('w'), white)
  'wp class'
class whiteRook(rook, white)
  'wR class'
  def __init__(self, side = 'undef')
    self.side = side
    if   str(side) == 'q':
      self.column = 0
    elif str(side) == 'k':
      self.column = 7
    else:
      self.column = -1
class whiteKnight(knight, white)
  'wN class'
  def __init__(self, side = 'undef')
    self.side = side
    if   str(side) == 'q':
      self.column = 1
    elif str(side) == 'k':
      self.column = 6
    else:
      self.column = -1
class whiteBishop(bishop, white)
  'wB class'
  def __init__(self, side = 'undef')
    self.side = side
    if   str(side) == 'q':
      self.column = 2
    elif str(side) == 'k':
      self.column = 5
    else:
      self.column = -1
class whiteQueen(queen, white)
  'wQ class'
class whiteKing(king, white)
  'wK class'

###########################################################
# Sides: Black
###########################################################
class blackPawn(pawn('b'), black)
  'bp class'
class blackRook(rook, black)
  'bR class'
  def __init__(self, side = 'undef')
    self.side = side
    if   str(side) == 'q':
      self.column = 0
    elif str(side) == 'k':
      self.column = 7
    else:
      self.column = -1
class blackKnight(knight, black)
  'bK class'
  def __init__(self, side = 'undef')
    self.side = side
    if   str(side) == 'q':
      self.column = 1
    elif str(side) == 'k':
      self.column = 6
    else:
      self.column = -1
class blackBishop(bishop, black)
  'bB class'
  def __init__(self, side = 'undef')
    self.side = side
    if   str(side) == 'q':
      self.column = 2
    elif str(side) == 'k':
      self.column = 5
    else:
      self.column = -1
class blackQueen(queen, black)
  'bQ class'
class blackKing(king, black)
  'bK class'
