# Darlene Fung
# 3/8/16

''' Takes a base and exponent and calculates the value of base raised to the power of the integer '''

def power(base, exponent):  
	if exponent == 0:		
		return 1
	else: 
		return base * power(base, exponent -1)