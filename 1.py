import argparse

# getting user`s input
parser = argparse.ArgumentParser('Calculate given expression')
parser.add_argument("expression", nargs='*')
args = parser.parse_args()

# using eval() to calcute given exression
args.expression = "".join(args.expression)
try:
    result = eval(args.expression)
    print(result)
except SyntaxError:
    print("\nError!")
except NameError:
    print("\nError!")