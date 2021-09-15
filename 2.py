import argparse
import operator

# getting user`s input
parser = argparse.ArgumentParser('Calculate given expression')
parser.add_argument("expression", nargs='*')
args = parser.parse_args()

# using eval() to calcute given argumets with given operation
result = eval("operator." + args.expression[0])(int(args.expression[1]), int(args.expression[2]))
print(result)
