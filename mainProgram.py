from powerFunctionRecursion import *				# import the function

def int_input(answer):
	'''checks that input is an integer '''
	try: 
		answer = int(answer)
		return answer
	except ValueError:
		answer = raw_input("You entered a string. Try again: ")
		return int_input(answer)
		
def float_input(answer):
	'''checks that input is a decimal '''
	try: 
		answer = int(answer)
		return answer
	except ValueError:
		answer = raw_input("You entered a string. Try again: ")
		return int_input(answer)
		
base = raw_input("What is your base? ")
checkedBase = int_input(base) 		
			
exponent = (raw_input("What is your exponent? "))	# asks for exponent
checkedExponent = int_input(exponent)

print("power({}, {}) -> {}".format(checkedBase, checkedExponent, power(checkedBase, checkedExponent))) # prints you base, exponent, and what the answer is(