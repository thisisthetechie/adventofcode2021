## Advent of Code 2021
## Day 10 Part 2
import aoc_core as aoc
import re, numpy, math
f = aoc.fd

bads = 0
tally = []

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
    else:
        s = ''.join(reversed(x))
        comp = 0
        for d in s:
            match d:
                case '(':
                    comp = (comp * 5) + 1
                case '[':
                    comp = (comp * 5) + 2
                case '{':
                    comp = (comp * 5) + 3
                case '<':
                    comp = (comp * 5) + 4
        tally.append(comp)

tally.sort()
print("Total points for bad scores =",bads)
print("Total points for completing =",tally[math.floor(len(tally)/2)])