import argparse

# getting user`s input
parser = argparse.ArgumentParser('Calculate given expression')
parser.add_argument("expression", nargs='*')
args = parser.parse_args()

# using eval() to calcute given exression
args.expression = "".join(args.expression)
print(eval(args.expression))
