import sys
#Make a program that takes a string as argument, reverses it, swaps its letters case and print the result.
res =''
if len(sys.argv) == 1:
    print('usage: python exec.py arg1 [arg2 ... argn]')
    exit(1)

nbrOfArguments = len(sys.argv)
for i in range(1, nbrOfArguments):
    res += sys.argv[i]
    if nbrOfArguments != 2 and i < nbrOfArguments -1:
        res += " "
res = res.swapcase()
print(res[::-1])