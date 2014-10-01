# In the file arithmetic.py, these function signatures are required

# add(int, int) -> int
# Returns the sum of the two input integers

# subtract(int, int) -> int
# Returns the second number subtracted from the first

# multiply(int, int) -> int
# Multiplies the two inputs together

# divide(int, int) -> float
# Divides the first input by the second, returning a floating point

# square(int) -> int
# Returns the square of the input

# cube(int) -> int
# Returns the cube of the input

# power(int, int) -> int
# Raises the first integer to the power of the second integer and returns the value.

# mod(int, int) -> int
# Returns the remainder when the first integer is divided by the second integer.

def add(num1, num2):
    """Returns the sum of the two input integers"""
    return num1 + num2

def subtract(num1, num2):
    """Returns the second number subtracted from the first"""
    return num1 - num2

def multiply(num1, num2):
    """Multiplies the two inputs together"""
    return num1 * num2

def divide(num1, num2):
    """Divides the first input by the second, returning a floating point"""
    return float(num1) / float(num2)

def square(num1):
    """Returns the square of the input"""
    return num1 * num1

def cube(num1):
    """ Returns the cube of the input"""
    return num1**3

def power(num1, num2):
    """Raises the first integer to the power of the second integer and returns the value"""
    return num1**num2

def mod(num1, num2):
    """Returns the remainder when the first integer is divided by the second integer."""
    return num1 % num2