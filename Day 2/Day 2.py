from collections import Counter


with open('input.txt') as f:
    data = f.read().strip().splitlines()
n_of_twos = 0
n_of_threes = 0
for row in data:
    counts = [j for i, j in Counter(row).most_common()]
    if 2 in counts:
        n_of_twos += 1
    if 3 in counts:
        n_of_threes += 1
print(n_of_twos*n_of_threes)
