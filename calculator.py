import time

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
	__version__ = '0.1.1'
	while True:
		print("\nSelect Operator")
		print("1.Add")
		print("2.Subtract")
		print("3.Multiply")
		print("4.Divide")
		print("5.Version")
		
		# Take input from the user 
		
		choice = int(input("Enter choice: "))
		
		if choice == 5:
			print('\nVersion: {}'.format(__version__))
		else:
			
			num1 = int(str(input("\nEnter first number: ")).replace(' ', ''))
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
				print("Invalid Input")
			
if __name__ == "__main__":
	main()