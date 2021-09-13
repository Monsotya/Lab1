import argparse
import operator

parser = argparse.ArgumentParser('Calculate given expression')
parser.add_argument("expression", nargs='*')
args = parser.parse_args()

result = eval("operator." + args.expression[0])(int(args.expression[1]), int(args.expression[2]))
print(result)