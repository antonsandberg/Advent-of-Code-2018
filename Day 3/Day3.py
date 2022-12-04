import numpy as np


with open('input.txt') as f:
    data = f.readlines()

# preprocessing data
instructions = dict()
instructions['start_coords'] = []
instructions['size'] = []
for instruction in data:
    instruction = instruction.split()
    start_coords = instruction[2].split(",")
    start_coords[1] = start_coords[1][:-1]

    start_coords = [int(x) for x in start_coords]
    instructions['start_coords'].append(start_coords)

    size = instruction[3].split("x")
    size = [int(x) for x in size]
    instructions['size'].append(size)

# Part 1
tiles = np.zeros((1000, 1000))
for (start_coords, spread) in zip(instructions['start_coords'], instructions['size']):

    x, y = start_coords[0], start_coords[1]
    
    dx, dy = spread[0], spread[1]
    tiles[x:x+dx, y:y+dy] += 1
print(f'Day 3 part 1: {np.sum(tiles > 1)}')


# Part 2 (cheated a bit but np.all solution was too clean)
for i, (start_coords, spread) in enumerate(zip(instructions['start_coords'], instructions['size'])):

    x, y = start_coords[0], start_coords[1]
    
    dx, dy = spread[0], spread[1]
    if np.all(tiles[x:x+dx, y:y+dy] == 1):
        print(f'Day 3 part 2: {i+1}')


