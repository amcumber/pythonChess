#!/usr/bin/python
from header import *
from board import *
from pieces import *
from players import *

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

# wp0 = wp1 = wp2 = wp3 = wp4 = wp5 = wp6 = wp7 = whitePawn
# wp0.column = 0
# wp1.column = 1
# wp2.column = 2
# wp3.column = 3
# wp4.column = 4
# wp5.column = 5
# wp6.column = 6
# wp7.column = 7
#
# bp0 = bp1 = bp2 = bp3 = bp4 = bp5 = bp6 = bp7 = blackPawn
# bp0.column = 0
# bp1.column = 1
# bp2.column = 2
# bp3.column = 3
# bp4.column = 4
# bp5.column = 5
# bp6.column = 6
# bp7.column = 7
#
# wQR = whiteRook('q')
# wKR = whiteRook('k')
# wQR = blackRook('q')
# wKR = blackRook('k')
#
# wQR = whiteBishop('q')
# wKR = whiteBishop('k')
# wQR = blackBishop('q')
# wKR = blackBishop('k')
#
# wQR = whiteKnight('q')
# wKR = whiteKnight('k')
# wQR = blackKnight('q')
# wKR = blackKnight('k')
#
# wQR = whiteQueen
# wQR = blackQueen
#
# wQR = whiteKing
# wQR = blackKing

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
