## Advent of Code 2021
## Day 2 Part 1
import aoc_core as aoc
f = aoc.fd

h = 0
d = 0
for x in f:
    match x.split()[0]:
        case 'forward':
            h = h + int(x.split()[1])
        case 'down':
            d = d + int(x.split()[1])
        case 'up':
            d = d - int(x.split()[1])
print ('The final location is ' + str(h * d))
