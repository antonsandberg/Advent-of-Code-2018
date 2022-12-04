import numpy as np
import time
def main():
    with open('input.txt') as f:
        data = f.read().split('\n')

    # Preprocessing
    data = [x.split(',') for x in data]
    points = [(int(x), int(y)) for (x, y) in data]

    max_x = 0
    max_y = 0

    for x, y in points:
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    grid = np.zeros((max_x, max_y))

t1 = time.perf_counter()

t2 = time.perf_counter()

print(f'Time taken: {(t2-t1):.6f}s')
