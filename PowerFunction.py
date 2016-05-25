# Darlene Fung
# 3/8/16


def power(base, exponent):  # takes in 2 variables, a base and an exponent
	''' Takes a base and exponent and calculates the value of base raised to the power of the integer '''
	counter = 1				# keeps track of how many times the base as been multiplied
	rememberNumber = base	# when program starts, the number you are multiplying is the base
	if exponent == 0:		# if the exponent is 0, the answer is always 1
		return 1
	while counter != exponent: 	# if the exponent is not equal to the counter (so is not equal to 1, because the counter is set to 1 initially) 
		rememberNumber = rememberNumber * base # the new number being multiplied is compiled
		counter += 1		# counter increases by 1 to keep track of the number times the base has been multiplied
	return rememberNumber 	# when loop ends, it returns the most recent rememberNumber, which is the final answer 
	
base = int(raw_input("What is your base? "))			# asks for base
exponent = int(raw_input("What is your exponent? "))	# asks for exponent

print("power({}, {}) -> {}".format(base, exponent, power(base,exponent))) # prints you base, exponent, and what the answer is



	
