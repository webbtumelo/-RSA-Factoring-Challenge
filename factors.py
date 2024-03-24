#!/usr/bin/python3

import sys

def factors(num):
	n = 2
	if num < 2:
		return
	while num % n:
		n = n + 1
	print(f"{num:.0f} = {num / n:.0f } * {n:.0f}")
if len(sys.argv) != 2:
	sys.exit()
try:
	with open(argv[1]) as file:
		l = file.readline()
		for l in file:
			num = int(l.strip())
			factors(num)
except:
	pass
