## Advent of Code 2021
## Day 7 Part 1
import aoc_core as aoc
import numpy
f = aoc.fd

f = [int(i) for i in f[0].split(',')]
fuel = numpy.zeros(max(f)+1,int)
def getFuel(start,end):
    consumed = 0
    consumed += (abs(start-end)*(abs(start-end)+1))/2
    return consumed

for target in range(max(f)+1):
    for crab in f:
        fuel[target] += getFuel(crab,target)
print (numpy.min(fuel))
print (numpy.where(fuel == numpy.min(fuel)))

