## Advent of Code 2021
## Day 5 Part 1
import aoc_core as aoc
import re
import numpy
f = aoc.fd
chartHeight = len(f)
chartData = []
for v in f:
    tmp = re.split(',| -> ',v)
    chartData.append(tmp)
chartData = numpy.array(chartData).astype(int)
chartMax = chartData.max()+1
chartOut = numpy.zeros((chartMax,chartMax),int)
for v in chartData:
    if (v[0] == v[2]):
        step = 1 if v[1]<v[3] else -1
        x = v[0]
        y = range(v[1],v[3]+step,step)
        for row in y:
            chartOut[row][x] += 1
    elif (v[1] == v[3]):
        step = 1 if v[0]<v[2] else -1
        x = range(v[0],v[2]+step,step)
        y = v[1]
        for col in x:
            chartOut[y][col] += 1
print (chartOut)
print ("Total number of overlaps:",numpy.count_nonzero(chartOut>1))
