def add(a,b):
	return a+b
def subtract(a,b):
	return a-b
def multiply(a,b):
	return a*b
def divide(a,b):
	return a/b

while True:
	print("\nOptions: ")
	print("Enter '+' to add two numbers")
	print("Enter '-' to subtract two numbers")
	print("Enter '*' to multiply two numbers")
	print("Enter '/' to divide two numbers")
	print("Enter 'q' to quit two numbers")
	
	user_input = input(": ")
	
	if user_input == 'q':
		break
	
	elif user_input in ['+','-','*','/']:
		
		try: 
			num1 = float(input("Enter the first number: "))
			num2 = float(input("Enter the second number: "))
			if user_input == '+':
				print(f'The result is: {add(num1,num2)}')
			elif user_input == '-':
				print(f'The result is: {subtract(num1,num2)}')
			elif user_input == '*':
				print(f'The result is: {multiply(num1,num2)}')
			elif user_input == '/':
				print(f'The result is: {divide(num1,num2)}')
		except (ValueError, ZeroDivisionError) as e:
			print(f'Error Type: {e}! Start over!')

	else:
		print("Unknown input!")	