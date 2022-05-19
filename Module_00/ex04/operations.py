import sys


def check_arg(arg):
    if len(arg) > 3:
        print('InputError: too many arguments')
        exit(1)
    elif len(arg) < 2:
        print('USAGE: : python operations.py <number1> <number2>')
        exit(1)


def do_operations(lhs, rhs):
    print("Sum:        %d" % lhs + rhs)
    print("Difference: %d" % lhs - rhs)
    print("Product:    %d" % lhs * rhs)
    print("Quotient:   %d" % lhs / rhs)
    print("Remainder:  %d" % lhs % rhs)
    
check_arg(sys.argv)
print(type(sys.argv[1]))
lhs = int(sys.argv[1])
rhs = int(sys.argv[2])
# do_operations(lhs,rhs)
