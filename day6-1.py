## Advent of Code 2021
## Day 6 Part 1
import aoc_core as aoc
import re
import numpy
f = aoc.fd

fishData = [int(i) for i in f[0].split(',')]
noDays = 80
gesPeriod = 8
for fishCount in range(noDays):
    for fish in range(len(fishData)):
        if fishData[fish] == 0:
            fishData.append(8)
            fishData[fish] = 6
        else:
            fishData[fish] -= 1
print ("Count of fish after",noDays,"days:",len(fishData))