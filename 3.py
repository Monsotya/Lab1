formula = input("Enter expression\n")
formula = formula.replace(" ", "")
length = len(formula) - 1
isFormula = True

# checks if there is a line
if formula == "":
    isFormula = False
    print("\nresult = (" + str(isFormula) + ", None)")

# checks for wrong number of signs
elif formula.find("++") != -1 or formula.find("--") != -1:
    isFormula = False
    print("\nresult = (" + str(isFormula) + ", None)")

# checks if formula starts and ends in a number
elif not(formula[0].isdigit() and formula[length].isdigit()):
    isFormula = False
    print("\nresult = (" + str(isFormula) + ", None)")
else:
    buffer = formula.replace("+", "")
    buffer = buffer.replace("-", "")
    if buffer.isdigit():
        result = eval(formula)
        print("\nresult = (" + str(isFormula) + ", " + str(result) + ")")
    else:
        isFormula = False
        print("\nresult = (" + str(isFormula) + ", None)")
