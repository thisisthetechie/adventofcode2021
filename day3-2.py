## Advent of Code 2021
## Day 3 Part 2
f = [l.rstrip() for l in open('day3.txt')]
print ("There are " + str(len(f)) + " values")

def calculateRating(method):
    d = f
    match method:
        case "Carbon":
            defaultVal = "0"
            useVal = "1"
        case "Oxygen":
            defaultVal = "1"
            useVal = "0"
    for col in range(0,len(d[0])):
        e = []
        colCount = 0
        for row in range(0,len(d)):
            colCount = colCount + int(d[row][col])
        colVal = defaultVal
        if (colCount < (len(d)/2)):
            colVal = useVal

        for row in range(0,len(d)):
            if (d[row][col] == colVal):
                e.append(d[row])
        if (len(e) > 0):
            d = e
        else:
            continue
    outputValue = ''.join(d)
    print (method + " = " + str(outputValue))
    return outputValue

o2  = calculateRating("Oxygen")
co2 = calculateRating("Carbon")

# Output the Rating
print ("Oxygen Rating = " + str(int(o2,2) * int(co2,2)))
