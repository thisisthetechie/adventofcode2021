## Advent of Code 2021
## Day 1 Part 1
f = [l.rstrip() for l in open('day1.txt')]
y = f[0]
d = 0
print (y + " (Initial Value)")
for x in f[1:]:
    if (int(x) > int(y)):
        print (x + " (Increased)")
        d = d+1
    else:
        print (x + " (Decreased)")
    y = x
print ("There were " + str(d) + " increases")