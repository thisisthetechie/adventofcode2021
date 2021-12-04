## Advent of Code 2021
## Day 1 Part 2
import aoc_core as aoc
f = aoc.fd

y = 0
d = 0
for x in range(2, len(f)):
    v = int(f[x]) + int(f[x-1]) + int(f[x-2]) 
    if (int(y) == 0):
        print (str(v) + " (Initial Value)")
    elif (int(v) > int(y)):
        print (str(v) + " (Increased)")
        d = d+1
    else:
        print (str(v) + " (Decreased)")
    y = v
print ("There were " + str(d) + " increases")