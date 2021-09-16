import argparse

# getting user`s input
parser = argparse.ArgumentParser('Calculate given expression')
parser.add_argument("expression", nargs='*')
args = parser.parse_args()

# using eval() to calculate given expression
args.expression = "".join(args.expression)
try:
    result = eval(args.expression)
    print(result)
except SyntaxError:
    print("\nError with string!")
except NameError:
    print("\nError with names!")