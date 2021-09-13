formula = input("Enter expression\n")
length = len(formula) - 1

if formula[0].isdigit() and formula[0].isdigit():
    while length >= 0:
        if formula[length].isdigit():
            length -= 1
        elif formula[length] == '-' or formula[length] == '+':
            if formula[length + 1] == '-' or formula[length + 1] == '+':
                print("result = (False, None)")
                break
            length -= 1
        else:
            print("result = (False, None)")
            break
    if formula.isdigit():
        print("result = (True, " + formula + ")")
    else:
        result = eval(formula)
        print("result = (True, " + str(result) + ")")
else:
    print("result = (False, None)")


