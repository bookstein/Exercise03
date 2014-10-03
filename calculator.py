"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
import arithmetic_mytry

def main():

    arithmetic_functions = {
    '+': arithmetic.add,
    '-': arithmetic.subtract,
    '*': arithmetic.multiply,
    '/': arithmetic.divide,
    'pow': arithmetic.power,
    'square': arithmetic.square,
    'cube': arithmetic.cube,
    'mod': arithmetic.mod,
    }

    while True:
        # get user input
        user_input = raw_input("> ")

        # turn user input into a list
        tokens = user_input.split()

        cmd = tokens[0]
        # check if first item is Q or q
        if cmd == "q" or cmd == "Q":
            break

        if cmd in arithmetic_functions:
            # try / except -- check validity of input
            try:
                for idx in range(1, len(tokens)):
                    if tokens[idx] == "0":
                       tokens[idx] = int(tokens[idx])
                    if float(tokens[idx]):
                        tokens[idx] = float(tokens[idx])
                        #print tokens[idx]


            except:
                print "Please enter valid numbers. Try again"
                continue

            # use dictionary and dispatch method to call function
            print arithmetic_functions[cmd](tokens[1:])

        else:
            print "That was not a valid entry. Please choose a valid mathematical operation from the following list:"
            for key in arithmetic_functions:
                print key


if __name__ == '__main__':
    main()