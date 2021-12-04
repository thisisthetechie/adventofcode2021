## Advent of Code 2021
## Day 2 Part 2
import aoc_core as aoc
f = aoc.fd

h = 0
d = 0
a = 0
for x in f:
    print (x)
    match x.split()[0]:
        case 'forward':
            h = h + int(x.split()[1])
            d = d + (a * int(x.split()[1]))
            print (' - Horizontal ' + str(h))
            print (' - Depth ' + str(d))
            print (' - Aim ' + str(a))
        case 'down':
            a = a + int(x.split()[1])
            print (' - Horizontal ' + str(h))
            print (' - Depth ' + str(d))
            print (' - Aim ' + str(a))
        case 'up':
            a = a - int(x.split()[1])
            print (' - Horizontal ' + str(h))
            print (' - Depth ' + str(d))
            print (' - Aim ' + str(a))
print ('The final location is ' + str(h * d))
