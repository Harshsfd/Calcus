# Project Calculator in Python TASK 2
# Intern ID- CC51345
# Harsh Bhardwaj 
# Mail: harshbhardwaj1511@gmail.com 
# Designation- Python Development Intern
# Batch- August 2023
# Import the necessary modules.
import math

# Define the functions that will perform the calculations.
print('\033[97mThis is white text.\033[0m')
def add(x, y):
  """Adds two numbers together."""
  return x + y

def subtract(x, y):
  """Subtracts one number from another."""
  return x - y

def multiply(x, y):
  """Multiplies two numbers together."""
  return x * y

def divide(x, y):
  """Divides one number by another."""
  return x / y

# Get the input from the user.
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# Choose the operation that you want to perform.
operation = input("Enter the operation you want to perform (+, -, *, /): ")

# Perform the calculation.
if operation == "+":
  result = add(x, y)
elif operation == "-":
  result = subtract(x, y)
elif operation == "*":
  result = multiply(x, y)
elif operation == "/":
  result = divide(x, y)

# Print the result.
print("The result is:", result)