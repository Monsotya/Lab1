formula = input("Enter expression\n")
formula = formula.replace(" ", "")
length = len(formula) - 1
isFormula = True

# checks if there is a line
if formula == "":
    isFormula = False
    print("\nresult = (" + str(isFormula) + ", None)")

# checks if formula starts and ends in a number
elif formula[0].isdigit() and formula[length].isdigit():
    while length >= 0:
        if formula[length].isdigit():
            length -= 1
        # checks if the expression contains wrong number of signs
        elif formula[length] == '-' or formula[length] == '+':
            if formula[length + 1] == '-' or formula[length + 1] == '+':
                isFormula = False
                print("\nresult = (" + str(isFormula) + ", None)")
                break
            length -= 1
        # checks for other symbols
        else:
            isFormula = False
            print("\nresult = (" + str(isFormula) + ", None)")
            break
else:
    isFormula = False
    print("\nresult = (" + str(isFormula) + ", None)")

# if the expression is a formula, it`s calculated with eval()
if isFormula:
    result = eval(formula)
    print("\nresult = (" + str(isFormula) + ", " + str(result) + ")")
