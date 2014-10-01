"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
import arithmetic

def main():

    while True:
        user_input = raw_input("> ")
        tokens = user_input.split()
        if tokens[0] == 'q':
            break

        try:
            cmd, number1, number2 = tokens[0], float(tokens[1]), float(tokens[2])
        except ValueError:
            print "This calculator can only calculate numbers."
            continue

        arithmetic_functions = {
            '+': arithmetic.add,
            '-': arithmetic.subtract,
            '*': arithmetic.multiply,
            '/': arithmetic.divide,
            'pow': arithmetic.power,
            'square': arithmetic.square,
            'cube': arithmetic.cube,
            'mod': arithmetic.mod
        }

        if cmd in arithmetic_functions:
            print arithmetic_functions[cmd](number1, number2)
        else:
            print "That is not a valid command. Try again. Format: Operation Number1 Number2"

   
if __name__ == '__main__':
    main()