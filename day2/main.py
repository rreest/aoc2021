#!/usr/bin/env python3

scores = {
    'AX': 4,    # rock + rock = 1 + 3
    'AY': 8,    # rock + paper = 2 + 6
    'AZ': 3,    # rock + scissors = 3 + 0
    'BX': 1,    # paper + rock = 1 + 0
    'BY': 5,    # paper + paper = 2 + 3
    'BZ': 9,    # paper + scissors = 3 + 6
    'CX': 7,    # scissors + rock = 1 + 6
    'CY': 2,    # scissors + paper = 2 + 0
    'CZ': 6     # scissors + scissors = 3 + 3
}

decisions = {
    'AX': scores['AZ'],    # rock + loss = scissors
    'AY': scores['AX'],    # rock + draw = rock
    'AZ': scores['AY'],    # rock + win = paper
    'BX': scores['BX'],    # paper + loss = rock
    'BY': scores['BY'],    # paper + draw = paper
    'BZ': scores['BZ'],    # paper + win = scissors
    'CX': scores['CY'],    # scissors + loss = paper
    'CY': scores['CZ'],    # scissors + draw = scissors
    'CZ': scores['CX']     # scissors + win = rock
}
data = [(x.strip().split(' ')) for x in open('input').readlines()]

print("Part 1: {}".format(sum(map(lambda x: scores["".join(x)], data))))
print("Part 2: {}".format(sum(map(lambda x: decisions["".join(x)], data))))
