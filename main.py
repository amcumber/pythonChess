#!/usr/bin/python
import classes.py
###########################################################
# TODO
# 2) board
# 3) enter move and update board
# 4) check if legal
# 5) check if check
# 6) add concede
# 7) add restart game
# 7) check if cm
# 8) Check check
# 9) castle check

###########################################################
# Init pieces
###########################################################

wp0 = wp1 = wp2 = wp3 = wp4 = wp5 = wp6 = wp7 = whitePawn
wp0.column = 0
wp1.column = 1
wp2.column = 2
wp3.column = 3
wp4.column = 4
wp5.column = 5
wp6.column = 6
wp7.column = 7

bp0 = bp1 = bp2 = bp3 = bp4 = bp5 = bp6 = bp7 = blackPawn
bp0.column = 0
bp1.column = 1
bp2.column = 2
bp3.column = 3
bp4.column = 4
bp5.column = 5
bp6.column = 6
bp7.column = 7

wQR = whiteRook('q')
wKR = whiteRook('k')
wQR = blackRook('q')
wKR = blackRook('k')

wQR = whiteBishop('q')
wKR = whiteBishop('k')
wQR = blackBishop('q')
wKR = blackBishop('k')

wQR = whiteKnight('q')
wKR = whiteKnight('k')
wQR = blackKnight('q')
wKR = blackKnight('k')

wQR = whiteQueen
wQR = blackQueen

wQR = whiteKing
wQR = blackKing

###########################################################
# Init Players
###########################################################

whitePlayer(white, player)
blackPlayer(black, player)
  #TODO

###########################################################
# Board
###########################################################

fullboard = [                               "\n\n",
 "\t    AA   BB   CC   DD   EE   FF   GG   HH    ",
 "\t  +----+----+----+----+----+----+----+----+  ",
 "\t8 |    | -- |    | -- |    | -- |    | -- | 8",
 "\t  +----+----+----+----+----+----+----+----+  ",
 "\t7 | -- |    | -- |    | -- |    | -- |    | 7",
 "\t  +----+----+----+----+----+----+----+----+  ",
 "\t6 |    | -- |    | -- |    | -- |    | -- | 6",
 "\t  +----+----+----+----+----+----+----+----+  ",
 "\t5 | -- |    | -- |    | -- |    | -- |    | 5",
 "\t  +----+----+----+----+----+----+----+----+  ",
 "\t4 |    | -- |    | -- |    | -- |    | -- | 4",
 "\t  +----+----+----+----+----+----+----+----+  ",
 "\t3 | -- |    | -- |    | -- |    | -- |    | 3",
 "\t  +----+----+----+----+----+----+----+----+  ",
 "\t2 |    | -- |    | -- |    | -- |    | -- | 2",
 "\t  +----+----+----+----+----+----+----+----+  ",
 "\t1 | -- |    | -- |    | -- |    | -- |    | 1",
 "\t  +----+----+----+----+----+----+----+----+  ",
 "\t    AA   BB   CC   DD   EE   FF   GG   HH    ",
                                            "\n\n"]

# print "%s%s's location is: %s%s with an attackset of %s" % (
#   wK.color, wK.piece, wK.columnname, wK.row, wK.atackset)
# print "%s%s" % (wKB.columnname, wKB.row)

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
