#!/usr/bin/python

# Function solves task 88.a MOO
def task88a( from_input ):
	from_input = from_input ** 2
	for check in str(from_input):
		if check == '3':
			return True