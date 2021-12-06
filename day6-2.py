## Advent of Code 2021
## Day 6 Part 2
import aoc_core as aoc
import re
import numpy
f = aoc.fd

initial = [int(i) for i in f[0].split(',')]
noDays = 256
gesPeriod = 8
fishCount = [0] * (gesPeriod+1)
for fish in initial:
    fishCount[fish] += 1
for rangeDays in range(noDays):
    fishTmp = [0] * (gesPeriod+1)
    for fish in range(1,gesPeriod+1):
        fishTmp[fish -1] = fishCount[fish]
    fishTmp[8] = fishCount[0] * 1
    fishTmp[6] += fishCount[0]

    fishCount = fishTmp    
print ("Count of fish after",noDays,"days:",sum(fishCount))