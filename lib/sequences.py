#!/usr/bin/env python3

def print_fibonacci(length):

    #initialise new list
	sequence = []
	
    #cater for length between 0 and 1 only first.
	if length > 0:
		sequence.append(0)
		
    #cater for length equal to 2 going up second.
	#firstly, if length = 2
	if length >= 2:
		sequence.append(1)
		
        #secondly, for length greater than 2
		for i in range(2, length):
			sequence.append(sequence[-1] + sequence[-2])

	print(sequence)
