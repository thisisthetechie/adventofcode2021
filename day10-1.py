## Advent of Code 2021
## Day 10 Part 1
import aoc_core as aoc
import re, numpy, math
f = aoc.fd

bads = 0

for x in f:
    #srch(x,')','(')
    for i in range(1000):
        x = re.sub('\(\)|\[\]|\<\>|\{\}','',x)
    r = re.search('\)|\>|\}|\]',x)
    if r:
        #print("bad",r.group())
        match r.group():
            case ')':
                bads += 3
            case ']':
                bads += 57
            case '}':
                bads += 1197
            case '>':
                bads += 25137

print("Total points for bad scores =",bads)