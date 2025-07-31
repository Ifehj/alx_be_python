def safe_divide(numerator, denominator):
	try:
		print(f"The result of the division is {numerator / denominator}")
	except ZeroDivisionError:
		print("Error: Cannot divide by zero.")
	except TypeError:
		print("Error: Please enter numeric values only.")