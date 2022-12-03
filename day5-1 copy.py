## Advent of Code 2021
## Day 5 Part 1
import aoc_core as aoc
import re
import numpy
f = aoc.fe
chartHeight = len(f)
chartData = []
for v in f:
    tmp = re.split(',| -> ',v)
    chartData.append(tmp)
chartData = numpy.array(chartData).astype(int)
chartMax = chartData.max()+1
chartOut = numpy.zeros((chartMax,chartMax),int)
for v in chartData:
    stepX = 1 if v[0]<v[2] else -1
    stepY = 1 if v[1]<v[3] else -1
    if (v[0] == v[2]):
        stepY = 0
    elif (v[1] == v[3]):
        stepX = 0

    for count in range(abs(v[0]-v[2])+1):
            row = v[0]+(stepX * count)
            col = v[1]+(stepY * count)
            chartOut[col][row] += 1
print (chartOut)
print ("Total number of overlaps:",numpy.count_nonzero(chartOut>1))
