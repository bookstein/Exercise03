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

def add(*args):
    """Returns the sum of the two input integers"""
    total = 0
    for a in args:
        total = total + a
    return total

def subtract(*args):
    """Returns the second number subtracted from the first"""
    total = args[0]
    print args
    for a in args[1:]:
        total = total - a
        print total
    return total

def multiply(*args):
    """Multiplies the two inputs together"""
    total = 1
    for a in args:
        total = total * a
    return total

def divide(*args):
    """Divides the first input by the second, returning a floating point"""
    total = args[0]
    for a in args[1:]:
        total = total / a
    return total

def square(num1):
    """Returns the square of the input"""
    return num1**2

def cube(num1):
    """ Returns the cube of the input"""
    return num1**3

def power(*args):
    """Raises the first integer to the power of the second integer and returns the value"""
    total = args[0]
    for a in args[1:]:
        total = total ** a
    return total

def mod(*args):
    """Returns the remainder when the first integer is divided by the second integer."""
    total = args[0]
    for a in args[1:]:
        total = total % a
    return total