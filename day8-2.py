## Advent of Code 2021
## Day 8 Part 2
import aoc_core as aoc
import difflib
f = aoc.fe
count = 0
display = {
    "acedgfb"   : 8,
    "cdfbe"     : 5,
    "gcdfa"     : 2,
    "fbcad"     : 3,
    "dab"       : 7,
    "cefabd"    : 9,
    "cdfgeb"    : 6,
    "eafb"      : 4,
    "cagedb"    : 0,
    "ab"        : 1
}

print(''.join(sorted("acedgfb")))
for i in f:
    display = [0] * 10
    data = i.split('|')[0].strip()
    sample = sorted(data.split(), key=len)
    print (sample)
    for number in sample:
        print(''.join(sorted(number)))