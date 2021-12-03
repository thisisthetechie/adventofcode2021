## Advent of Code 2021
## Day 3 Part 2
f = [l.rstrip() for l in open('day3.txt')]
print ("There are " + str(len(f)) + " values")

# Get the Oxygen Value
d = f
for col in range(0,len(d[0])):
    e = []
    colCount = 0
    for row in range(0,len(d)):
        colCount = colCount + int(d[row][col])
    colVal = "1"
    if (colCount < (len(d)/2)):
        colVal = "0"

    for row in range(0,len(d)):
        if (d[row][col] == colVal):
            e.append(d[row])
    if (len(e) > 0):
        d = e
    else:
        continue

print ("Oxygen = " + str(d))
o2 = ''.join(d)

# Get the Carbon Dioxide Value
d = f
for col in range(0,len(d[0])):
    e = []
    colCount = 0
    for row in range(0,len(d)):
        colCount = colCount + int(d[row][col])
    colVal = "0"
    if (colCount < (len(d)/2)):
        colVal = "1"

    for row in range(0,len(d)):
        if (d[row][col] == colVal):
            e.append(d[row])
    if (len(e) > 0):
        d = e
    else:
        continue

print ("Carbon = " + str(d))
co2 = ''.join(d)

# Output the Rating
print ("Oxygen Rating = " + str(int(o2,2) * int(co2,2)))
