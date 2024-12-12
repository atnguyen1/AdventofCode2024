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

	# Do Combines
	combined_eval_list = []
	for e in eval_list:
		#print(e)
		combine_index = []

		d = e.copy()
		if '|' in d:				
			while '|' in d:
				z = d.index('|')
				first = d[z - 1]
				second = d[z + 1]
				comb = first + second

				first_half = d[:z - 1]
				second_half = d[z + 2:]
				new_d = first_half + [comb] + second_half
				d = new_d
		combined_eval_list.append(d)		

	results = []
	for e in combined_eval_list:
		d = e.copy()

		if len(d) > 1:
			first = str(d.pop(0))

			for c in divide_chunks(d, 2):
				exp = first + ' ' + ' '.join([str(x) for x in c])
				k = eval(exp)
				first = str(k)
			print(e, first)
			if int(first) == total:
				results.append(first)
				break
		else:
			print(d)
			if int(d[0]) == total:
				results.append(d[0])
				break

	if str(total) in results:
		sum_correct2 += total

print('Part 2:', sum_correct2)