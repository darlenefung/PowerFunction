from powerFunctionRecursion import power				# import the function

base = float(raw_input("What is your base? "))			# asks for base
exponent = int(raw_input("What is your exponent? "))	# asks for exponent

print("power({}, {}) -> {}".format(base, exponent, power(base,exponent))) # prints you base, exponent, and what the answer is