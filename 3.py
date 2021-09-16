formula = input("Enter expression\n")
formula = formula.replace(" ", "")
isFormula = True

# checks if there is a line
if not formula:
    isFormula = False

# checks for wrong number of signs
elif formula.find("++") != -1 or formula.find("--") != -1:
    isFormula = False

# checks if formula starts and ends in a number
elif not (formula[0].isdigit() and formula[-1].isdigit()):
    isFormula = False
else:
    buffer = formula.replace("+", "")
    buffer = buffer.replace("-", "")
    if not buffer.isdigit():
        isFormula = False

if isFormula:
    result = eval(formula)
    print("\nresult = (" + str(isFormula) + ", " + str(result) + ")")
else:
    print("\nresult = (" + str(isFormula) + ", None)")
