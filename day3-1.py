## Advent of Code 2021
## Day 3 Part 1
f = [l.rstrip() for l in open('day3.txt')]
g = ["0"] * len(f[0])
e = ["0"] * len(f[0])
n = [0] * len(f[0])
# Sum the values
for x in f:
    for b in range(0,len(f[0])):
        n[b] = n[b] + int(x[b])
print (n)
# Parse the values
for x in range(0,len(f)):
    for v in range(0,len(f[0])):
        if (n[v] > (int(len(f)/2))):
            g[v] = "1"
            e[v] = "0"
        else:
            g[v] = "0"
            e[v] = "1"
# Mux into proper Binary
g = ''.join(g)
e = ''.join(e)
print ("Gamma   = " + g + " (" + str(int(g,2)) + ")")
#print (int(g,2))
print ("Epsilon = " + e + " (" + str(int(e,2)) + ")")
#print (int(e,2))
print ("Power Consumption = " + str(int(g,2) * int(e,2)))
