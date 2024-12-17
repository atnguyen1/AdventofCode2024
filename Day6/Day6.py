import os
import sys
from collections import defaultdict
import numpy as np

field = []
with open('../AdventSecrets/2024/6/6.input.txt', 'r') as fh:
	for line in fh:
		line = line.split('\n')[0]   # Input has carriage returns
		field.append(list(line))

test = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''

field = [list(x) for x in test.split('\n')]
#field = [list(x) for x in field]

field = np.matrix(field)

class playermap:
	def __init__(self, field):
		self.visited = list()
		self.initmap = field
		self.field = field   # Numpy Array
		self.startx = None
		self.starty = None
		self.x = None
		self.y = None
		self.direction = None
		self.ymax, self.xmax = field.shape
		self.visted.append((self.y, self.x, self.direction))

		for y in range(0, self.ymax - 1):
			for x in range(0, self.xmax - 1):
				if self.field[y, x] == '^':
					self.starty = y
					self.startx = x
					self.y = y
					self.x = x
					self.direction = '^'

	def step(self):
		direction = {'^': [-1, 0],
					 '>': [0, 1],
					 'v': [1, 0],
					 '<': [0, -1]}

		d = direction[self.direction]

		new_y = self.y + d[0]
		new_x = self.x + d[1]

		if (new_y > self.ymax - 1) or (new_x > self.xmax - 1) or (new_y < 0) or (new_x < 0):
			# Off map
			field[self.y, self.x] = 'x'
			self.x = new_x
			self.y = new_y
			return 2
		elif field[new_y, new_x] == '#':
			# Rock
			return 1
		else:
			# Moved
			field[self.y, self.x] = 'x'
			field[new_y, new_x] = self.direction
			self.x = new_x
			self.y = new_y
			self.visted.append((self.y, self.x, self.direction))
			return 0

	def move_to_rock(self):
		status = -1

		while status <= 0:
			status = self.step()

		return status

	def turn(self):
		if self.direction == '^':
			self.direction = '>'
		elif self.direction == '>':
			self.direction = 'v'
		elif self.direction == 'v':
			self.direction = '<'
		elif self.direction == '<':
			self.direction = '^'

		self.field[self.y, self.x] = self.direction

	def move(self):
		status = -1

		while status <= 0:
			status = self.move_to_rock()
			if status == 1:
				self.turn()
				status = -1

	def block_move(self):
		status = -1

		while status <= 0:
			status = self.move_to_rock()
			if status == 1:

				self.turn()
				status = -1

	def count(self):
		path = 0
		for y in range(0, self.ymax):
			for x in range(0, self.xmax):
				if self.field[y, x] == 'x':
					path += 1
		return path

	def pprint(self):
		#print(self.field)
		for y in range(0, self.ymax):
			print(''.join(self.field[y, :].tolist()[0]))
		print('')

p = playermap(field)

#p.pprint()
p.move()
#p.pprint()
print('Part 1:', p.count())

