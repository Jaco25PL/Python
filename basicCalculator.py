# Basic Calculator in Python

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
    # Check if user is trying to divide by zero
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

# Main program starts here
print("Welcome to Basic Calculator")
print("---------------------------")

# Continuous loop to keep the calculator running until user decides to exit
while True:
    # Display the operation menu
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    # Get user's choice of operation
    choice = input("Enter choice (1/2/3/4/5): ")
    
    # Check if user wants to exit
    if choice == '5':
        print("Thank you for using Basic Calculator!")
        break  # This exits the while loop
    
    # Check if the choice is valid
    if choice not in ('1', '2', '3', '4'):
        print("Invalid input! Please try again.")
        continue  # This skips the rest of the loop and starts over
    
    # Get the two numbers from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Perform the selected operation
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    
    elif choice == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")