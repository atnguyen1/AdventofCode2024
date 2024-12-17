import os
import re
import sys
import numpy as np
from collections import deque, Counter

data = []
with open('../AdventSecrets/2024/13/13.input.txt', 'r') as fh:
	d = fh.read().split('\n\n')
	data = d

test = '''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279'''

test = test.split('\n\n')
data = test

class ClawMachine:
	def __init__(self, initstring):
		initstring = initstring.split('\n')
		a = re.match('Button A: X\+(\d+), Y\+(\d+)', initstring[0])
		b = re.match('Button B: X\+(\d+), Y\+(\d+)', initstring[1])
		prize = re.match('Prize: X\=(\d+), Y\=(\d+)', initstring[2])

		if a is None or b is None or prize is None:
			raise ValueError('Malformed ClawMachine String')

		self.x_goal = int(prize.group(1))
		self.y_goal = int(prize.group(2))

		self.a_x = int(a.group(1))
		self.a_y = int(a.group(2))
		self.b_x = int(b.group(1))
		self.b_y = int(b.group(2))

		self.mat = np.matrix([[self.a_x, self.a_y], [self.b_x, self.b_y]])

	def contents(self):
		print('Button A- X:', self.a_x, ' Y:', self.a_y)
		print('Button B- X:', self.b_x, ' Y:', self.b_y)
		print('Goal: X=', self.x_goal, ' Y=', self.y_goal)
		print(self.mat)

a = ClawMachine(data[0])
a.contents()