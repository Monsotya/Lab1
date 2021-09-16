import argparse
import operator

# getting user`s input
parser = argparse.ArgumentParser('Calculate given expression')
parser.add_argument("expression", nargs='*')
args = parser.parse_args()

# using eval() to calculate given arguments with given operation

try:
    result = eval("operator." + args.expression[0])(int(args.expression[1]), int(args.expression[2]))
    print(result)
except SyntaxError:
    print("\nError with string!")
except IndexError:
    print("\nError with number of values!")
except:
    print("\nError!")
