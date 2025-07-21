Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))
Operation = input("Choose the operation (+, -, *, /): ")

match Operation:
	case "+":
		print(f"The result is: {Num1 + Num2}.")
	case "-":
		print(f"The result is: {Num1 - Num2}.")
	case "*":
		print(f"The result is: {Num1 * Num2}.")
	case "/":
		if Num2 != 0:
			print(f"The result is: {Num1 / Num2}.")
		else:
			print("Cannot divide by zero.")
	case _:
		print("Invalid operation. Please enter +, -, *, or /.")