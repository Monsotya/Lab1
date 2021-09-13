import argparse

parser = argparse.ArgumentParser('Calculate given expression')
parser.add_argument("expression", nargs='*')
args = parser.parse_args()

args.expression = "".join(args.expression)
print(eval(args.expression))

