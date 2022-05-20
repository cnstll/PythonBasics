import sys


def check_arg(arg):
    if len(arg) > 3:
        print('InputError: too many arguments.')
        exit(1)
    elif len(arg) < 2:
        print('USAGE: : python operations.py <number1> <number2>')
        exit(1)


def do_operations(lhs, rhs):
    try:
        print("Sum:        %d" % (lhs + rhs))
        print("Difference: %d" % (lhs - rhs))
        print("Product:    %d" % (lhs * rhs))
        print("Quotient:   %f" % (lhs / rhs))
        print("Remainder:  %d" % (lhs % rhs))
    except ZeroDivisionError:
        print("Quotient:   %s" % ("ERROR (div by zero)"))
        print("Remainder:  %s" % ("ERROR (modulo by zero)"))


check_arg(sys.argv)
try:
    lhs = int(sys.argv[1])
    rhs = int(sys.argv[2])
    do_operations(lhs, rhs)
except ValueError:
    print("InputError: only numbers.")
