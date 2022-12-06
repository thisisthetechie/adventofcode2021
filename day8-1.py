## Advent of Code 2021
## Day 8 Part 1
import aoc_core as aoc
import numpy
f = aoc.fd
count = 0
for i in f:
    data = i.split('|')[1].strip()
    for d in data.split():
        if len(d) in (2,3,4,7):
            count += 1

print ("There are ",count,"instances of 1, 4, 7 or 8")