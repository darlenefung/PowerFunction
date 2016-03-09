


# Darlene Fung
# 3/8/16

#	""" Takes a base and exponent and calculates the value of base raised to the power of the integer """



#def plus_ten(x):
#	return x + 10
#print plus_ten(44)


	


def power(base, exponent): 
	counter = 1
	rememberNumber = base
	if exponent == 0:
		return 1
	while counter != exponent: 
		rememberNumber = rememberNumber * base 
		counter += 1
	
	return rememberNumber 
	
base = int(raw_input("What is your base? "))
exponent = int(raw_input("What is your exponent? "))
	
print power(base, exponent)


#currentValue = base

#if exponent == 1:
#	print(base) 
	
#while exponent != 1 and exponent != 0: 
#while counter != exponent = 1:
#	rememberNumber = currentValue
#	currentValue = rememberNumber * base
#	counter += 1
	
	
