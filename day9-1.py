## Advent of Code 2021
## Day 9 Part 1
import aoc_core as aoc
import numpy
f = aoc.fe
gridWidth = len(f[0])
for d in range(len(f)):
    f[d] = list(f[d])
grid = numpy.array(f,int).reshape((len(f),gridWidth))
print (grid)
