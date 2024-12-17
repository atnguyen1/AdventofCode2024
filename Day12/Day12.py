import os
import sys
import numpy as np
from collections import deque, Counter

class field:
    def __init__(self, plots, veg):
        self.field = np.matrix(plots)
        self.max_y, self.max_x = self.field.shape
        self.veg_list = veg

    def find_bounds(self, x, y):

    def get_neighbors(self, x, y, neighbors):
        #neighbors = []
        directions = {'N': [-1, 0], 'E': [0, 1], 'S': [1, 0], 'W': [0, -1]}




data = []
with open('../AdventSecrets/2024/12/12.input.txt', 'r') as fh:
    for line in fh:
        line = line.rstrip()
        l = list(line)
        data.append(l)

test = '''AAAA
BBCD
BBCC
EEEC'''


data = [list(x) for x in test.split('\n')]

c = Counter()
for row in data:
    for p in row:
        c[p] += 1

f = field(data, c.keys())





