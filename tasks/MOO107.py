#!/usr/bin/python

# Function solves task 107 MOO
def task107( from_input ):
	quad_max = 1
	checker = 4
	result = 1
	for quad_max in range( from_input + 1 ):
		if checker ** quad_max < from_input:
			result = quad_max
	return result