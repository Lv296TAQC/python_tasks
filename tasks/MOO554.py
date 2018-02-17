#!/usr/bin/python

# Function solves task 554 MOO
def task554( from_input ):
	a = 0
	b = 0
	c = 0
	key = 1
	result = {}
	for c in range( from_input ):
		for b in range( c ):
			for a in range ( b ):
				if c**2 == a**2 + b**2:
					result[key] = [a, b, c]
					key += 1
	return result