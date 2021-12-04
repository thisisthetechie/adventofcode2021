## Advent of Code 2021
## Day 4 Part 1
import aoc_core as aoc
from collections import Counter
import numpy
f = aoc.fd

calledNumbers = f[0].split(',')

board = []
for i in range(2,len(f)):
    if (f[i] != ""):
        board.append(f[i].split())
boardCount = int(len(board)/5)
board = numpy.reshape(board,(boardCount,5,5))
def checkNumbers(board):
    for n in calledNumbers:
        board = numpy.where(board == n, 'x', board)
        for boardNo in range(boardCount):
            for row in range(5):
                if (numpy.char.count(board[boardNo][row], 'x').sum() == 5) or (numpy.char.count(numpy.swapaxes(board,1,2)[boardNo][row], 'x').sum() == 5):
                    board = numpy.where(board == 'x', 0, board)
                    boardSum = board[boardNo].astype(int).sum()
                    return (boardSum * int(n))

print ("Winning Value =",checkNumbers(board))
