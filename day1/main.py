#!/usr/bin/env python3
from itertools import chain

data = [[int(z) for z in x.split('\n')] for x in open('input').read().split('\n\n')]

print("Part 1: {}".format(max([sum(x) for x in data])))
print("Part 2: {}".format(sum(sorted([sum(x) for x in data])[-3:])))
