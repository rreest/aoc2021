#!/usr/bin/env python3
import os
import shutil

data = [x.strip().split(' ') for x in open('input').readlines()]

shutil.rmtree('root', ignore_errors=True)
os.mkdir('root')
os.chdir('root')
for c in data[1:]:
    print(f"pwd: {os.curdir}")
    if c[0] == 'dir':
        print(f"mkdir {c[1]}")
        os.mkdir(c[1])
    elif c[0].isnumeric():
        print(f"create file {c[1]}")
        with open(c[1], mode='wb') as f:
            f.truncate(int(c[0]))
    elif len(c) == 3 and c[1] == 'cd':
        os.chdir(c[2])

os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Part 1: Go to the project directory and execute the following command
# find root/ -type d -exec bash -c "find \"{}\" -type f -print0 | du -scb --files0-from=- | tail -n 1 | sed 's/\t.*//'" \; | awk '$1 < 100000 { s+=$1 } END { print s }'

# Part 2
data = [int(x) for x in open('du-precalculated').readlines()]
print(min(data, key=lambda x: abs(x-(30000000-(70000000-data[-1])))))
