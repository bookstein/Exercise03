"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
import arithmetic

def main():
    # Your code goes here
    
    # No setup
    # repeat forever:
    while True:
    #     read input
        input = raw_input("> ")
        #     tokenize input
        tokens = input.split(" ")
        if tokens[0] == 'q':
            break
        cmd, number1, number2 = tokens[0], int(tokens[1]), int(tokens[2])
        if cmd == '+':
            print arithmetic.add(number1, number2)
        elif cmd == '-':
            print arithmetic.subtract(number1, number2)
        elif cmd == '*':
            print arithmetic.multiply(number1, number2)
        elif cmd == '/':
            print arithmetic.divide(number1, number2)
        elif cmd == 'pow':
            print arithmetic.power(number1, number2)
        elif cmd == 'square':
            print arithmetic.square(number1, number2)
        elif cmd == 'cube':
            print arithmetic.cube(number1, number2)
        elif cmd == 'mod':
            print arithmetic.mod(number1, number2)
        else:
            print "I don't understand"

    #     if the first token is 'q', quit
    #     otherwise decide which math function to call based on the tokens we read


if __name__ == '__main__':
    main()