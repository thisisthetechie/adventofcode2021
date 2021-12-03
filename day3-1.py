## Advent of Code 2021
## Day 3 Part 1
f = [l.rstrip() for l in open('day3.txt')]
print ("There are " + str(len(f)) + " lines in our data")

def calculatePower(method):
    d = f
    outputValue = ""
    match method:
        case "Epsilon":
            defaultVal = "0"
            useThisVal = "1"
        case "Gamma":
            defaultVal = "1"
            useThisVal = "0"
    for col in range(0,len(d[0])):
        e = []
        colCount = 0
        for row in range(0,len(d)):
            colCount = colCount + int(d[row][col])
        colVal = defaultVal
        if (colCount < (len(d)/2)):
            colVal = useThisVal

        outputValue = outputValue + colVal
    print ('{:<7} = '.format(method) + str(outputValue) + " (" + str(int(outputValue,2)) + ")")
    return outputValue

gamma   = calculatePower("Gamma")
epsilon = calculatePower("Epsilon")
print ("Power Consumption = " + str(int(gamma,2) * int(epsilon,2)))
