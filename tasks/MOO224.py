#!/usr/bin/python

# Function solves task 224 MOO
def task224( from_input ):
	result = []
	try_natural = 1
	for try_natural in range(1, from_input + 1):
		if from_input % try_natural == 0:
			result.append(try_natural)
	return result