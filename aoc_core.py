import os.path
import sys

today = os.path.splitext(os.path.basename(sys.argv[0]).split('-')[0])[0]
part  = os.path.splitext(os.path.basename(sys.argv[0]).split('-')[1])[0]

fd = [l.rstrip() for l in open(today + '.txt')]
fe = [l.rstrip() for l in open(today + '-example.txt')]
print ('{:-^31}'.format("\U0001F384" + "Advent of Code 2021"))
print ('{:-^32}'.format(today.capitalize() + " Part" + part))