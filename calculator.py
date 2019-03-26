# This function adds two numbers 
def add(x, y):
	return x + y

# This function subtracts two numbers 
def subtract(x, y):
	return x - y

# This function multiplies two numbers
def multiply(x, y):
	return x * y

# This function divides two numbers
def divide(x, y):
	return x / y

def main():
	print("Select operation.")
	print("1.Add")
	print("2.Subtract")
	print("3.Multiply")
	print("4.Divide")
	
	# Take input from the user 
	choice = int(input("Enter choice(1/2/3/4):"))
	
	num1 = int(str(input("Enter first number: ")).replace(' ', ''))
	num2 = int(str(input("Enter second number: ")).replace(' ', ''))
	
	if choice == 1:
		print('{} + {} = {}'.format(num1, num2, add(num1,num2)))
		return add(num1,num2)
	
	elif choice == 2:
		print('{} - {} = {}'.format(num1, num2, subtract(num1,num2)))
		return subtract(num1,num2)
	elif choice == 3:
		print('{} x {} = {}'.format(num1, num2, multiply(num1,num2)))
		return multiply(num1,num2)
	elif choice == 4:
		print('{} / {} = {}'.format(num1, num2, divide(num1,num2)))
		return divide(num1,num2)
	else:
		print("Invalid input")