# Darlene Fung
# 4/11/16

''' Takes a base and exponent and calculates the value of base raised to the power of the integer '''

def power(base, exponent):  						# define the function 
	if exponent == 0:								# covers special case and last time the exponent needs to be multiplied 
		return 1
	else: 											# keeps multiplying the base using recursion 
		return base * power(base, exponent -1)