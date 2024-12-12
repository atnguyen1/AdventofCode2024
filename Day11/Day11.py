import os
import sys
from collections import deque, defaultdict

data = ''
with open('../AdventSecrets/2024/11/11.input.txt', 'r') as fh:
    data = fh.read()

test = '''0 1 10 99 999'''

test2 = '''125 17'''

test3 = '''8'''

test4 = '''1'''

class stones:
    def __init__(self, stone_str):
        self.stones = [int(x) for x in stone_str.split(' ')]
        self.stones = deque(self.stones)

        stones2 = defaultdict(int)
        for s in self.stones:
            stones2[s] += 1

        self.stones2 = stones2
        self.blink = 0

    def print(self):
        print(self.stones)

    def update(self):
        new_stones = deque()

        for s in self.stones:
            if s == 0:
                new_stones.append(1)
            elif len(str(s)) % 2 == 0:
                s2 = str(s)
                first = s2[:int(len(s2) / 2)]
                second = s2[int(len(s2) / 2):]

                new_stones.append(int(first))
                new_stones.append(int(second))
            else:
                new_stones.append(s * 2024)
        self.stones = new_stones

    def update2(self):
        new_stones = list()

        for key in self.stones2:
            if key == 0:
                new_stones.append((1, self.stones2[key]))
            elif len(str(key)) % 2 == 0:
                s2 = str(key)
                first = s2[:int(len(s2) / 2)]
                second = s2[int(len(s2) / 2):]

                new_stones.append((int(first), self.stones2[key]))
                new_stones.append((int(second), self.stones2[key]))
            else:
                new_stones.append((key * 2024, self.stones2[key]))

        stones_dict = defaultdict(int)

        for n in new_stones:
            stones_dict[n[0]] += 1 * n[1]
        self.stones2 = stones_dict
        self.blink += 1

    def count_stones(self):
        count = 0
        for key in self.stones2:
            count += int(self.stones2[key])

        return count

s = stones(data)

for k in range(0, 25):
    #print(len(s.stones))
    #s.print()  
    s.update()

print('Part 1:', len(s.stones))

k = stones(data)

while k.blink < 75:
    k.update2()

print('Part 2:', k.count_stones())