"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
import arithmetic

def main():

    while True:
        input = raw_input("> ")
        tokens = input.split(" ")
        if tokens[0] == 'q':
            break
            
        try:
            cmd, number1, number2 = tokens[0], float(tokens[1]), float(tokens[2])
        except ValueError:
            print "This calculator can only calculate numbers."
            continue
        
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

   
if __name__ == '__main__':
    main()