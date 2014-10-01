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
        number1, number2 = int(tokens[1]), int(tokens[2])

        if tokens[0] == 'q':
            break
        elif tokens[0] == '+':
            print arithmetic.add(number1, number2)

    #     if the first token is 'q', quit
    #     otherwise decide which math function to call based on the tokens we read


if __name__ == '__main__':
    main()