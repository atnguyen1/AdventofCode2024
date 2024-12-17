import os
import sys
from itertools import product
from collections import deque

def divide_chunks(l, n):    
    # looping till length l
    for i in range(0, len(l), n): 
        yield l[i:i + n]

data = []
with open('../AdventSecrets/2024/7/7.input.txt', 'r') as fh:
	for line in fh:
		total, parts = line.split(':')
		total = int(total)
		parts = parts.lstrip().rstrip()
		parts = parts.split(' ')
		parts = [int(x) for x in parts]
		data.append((total, parts))

test = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''

data2 = []

for t in test.split('\n'):
	total, parts = t.split(':')
	total = int(total)
	parts = parts.lstrip().rstrip()
	parts = parts.split(' ')
	#parts = [int(x) for x in parts]
	data2.append((total, parts))


sum_correct = 0
for entry in data2:
	total = entry[0]
	elements = deque(entry[1])
	l = len(elements)

	op_list = []	
	for x in product('*+', repeat=l - 1):
		op_list.append(''.join(x))

	#print(total, l, elements, op_list)

	eval_list = []
	f = elements.popleft()

	for entry in op_list:
		ops = list(entry)
		#print(ops)
		s = [f]
		for z, e in enumerate(ops):
			s.append(e)
			s.append(elements[z])
		eval_list.append(s)

	results = []
	for e in eval_list:
		d = e.copy()
		first = str(d.pop(0))

		for c in divide_chunks(d, 2):
			exp = first + ' ' + ' '.join([str(x) for x in c])
			k = eval(exp)
			first = str(k)
		if int(first) == total:
			results.append(first)
			break

	if str(total) in results:
		sum_correct += total

print('Part 1:', sum_correct)


sum_correct2 = 0
for entry in data2:
	total = entry[0]
	elements = deque(entry[1])
	l = len(elements)

	op_list = []	
	for x in product('*+|', repeat=l - 1):
		op_list.append(''.join(x))

	print(total, l, elements, op_list)

	eval_list = []
	f = elements.popleft()

	for entry in op_list:
		ops = list(entry)
		#print(ops)
		s = [f]
		for z, e in enumerate(ops):
			s.append(e)
			s.append(elements[z])
		eval_list.append(s)

	results = []
	for e in eval_list:
		d = e.copy()

		first = str(d.pop(0))

		if '|' in d:

			while '|' in d:
				d2 = deque(e)
				first = d2.popleft()
				second = d2.popleft()
				third = d2.popleft()



				for c in divide_chunks(d, 2):
					exp = first + ' ' + ' '.join([str(x) for x in c])
					if '|' in exp:



					else:
						k = eval(exp)
						first = str(k)

			print(e, first)

			if int(first) == total:
				results.append(first)
				break
		else:
			for c in divide_chunks(d, 2):
				exp = first + ' ' + ' '.join([str(x) for x in c])
				k = eval(exp)
				first = str(k)
			if int(first) == total:
				results.append(first)
				break


	if str(total) in results:
		sum_correct2 += total

print('Part 2:', sum_correct2)