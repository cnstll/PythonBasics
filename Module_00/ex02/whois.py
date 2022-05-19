import sys
# Make a program that takes a number as argument,
# checks whether it is odd, even or zero, and print the result


def check_arg(arg):
    if len(arg) > 2:
        print('ERROR: more than one argument is provided.')
        exit(1)
    elif len(arg) != 2:
        print('USAGE: python exec.py num')
        exit(1)


def print_number_parity(num):
    if num == 0:
        print("I’m Zero.")
    elif num % 2 == 0:
        print("I’m Even.")
    else:
        print("I’m Odd.")
    print()


check_arg(sys.argv)
arg = sys.argv[1]
try:
    num = int(arg)
    print_number_parity(num)
except ValueError:
    print('ERROR: argument is not an integer.')
    exit(1)
