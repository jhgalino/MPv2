def differentiate(fxn: str):
    hasCoeff = False
    hasExp = False
    hasTrig = False
    diff = ""

    # separate string into three parts which containe exponent, coeff,
    # and the function inside the parentheses
    def splitByParentheses(function: str):
        function = function.replace("(", "~", 1)
        function = function[::-1].replace(")", "~", 1)
        function = function[::-1].split("~")
        return function

    tempFxn = splitByParentheses(fxn)

    if len(tempFxn) < 3:  # if x is the only one left, omit x
        return ""

    if tempFxn[0] != "" and tempFxn[0].isdecimal():
        hasCoeff = True
    elif tempFxn[0] != "" and tempFxn[0].isalpha():
        hasTrig = True

    if tempFxn[-1] != "" and tempFxn[-1][-1].isdecimal():
        hasExp = True

    # if fxn is (x)
    if tempFxn[1] == "x" and tempFxn[0] == "" and tempFxn[2] == "":
        return "1"

    if hasExp:
        if hasCoeff:  # change coeff and exp into ints, then calculate
            tempFxn[0] = int(tempFxn[0])
            tempFxn[2] = int(tempFxn[2][1])
            tempFxn[0] = tempFxn[0] * tempFxn[2]
            tempFxn[2] -= 1
            if tempFxn[2] == 1:
                tempFxn[2] = ""
            else:
                tempFxn[2] = "^{}".format(tempFxn[2])
            diff = "{}({}){}".format(tempFxn[0], tempFxn[1], tempFxn[2])
        else:
            tempFxn[0] = int(tempFxn[2][1])
            tempFxn[2] = int(tempFxn[2][1]) - 1
            if tempFxn[2] == 1:
                tempFxn[2] = ""
            else:
                tempFxn[2] = "^{}".format(tempFxn[2])
            diff = "{}({}){}".format(tempFxn[0], tempFxn[1], tempFxn[2])
    elif hasTrig:
        if tempFxn[0] == "sin":
            diff = "({}({}))".format("cos", tempFxn[1])
        elif tempFxn[0] == "cos":
            diff = "({}({}))".format("-sin", tempFxn[1])
        elif tempFxn[0] == "tan":
            diff = "({}({})^2)".format("sec", tempFxn[1])
        elif tempFxn[0] == "sec":
            diff = "(sec({})tan({}))".format(tempFxn[1], tempFxn[1])
        elif tempFxn[0] == "csc":
            diff = "(-csc({})cot({}))".format(tempFxn[1], tempFxn[1])
        elif tempFxn[0] == "cot":
            diff = "(-csc({})^2)".format(tempFxn[1])

    diff = "{}*{}".format(diff, differentiate(tempFxn[1]))

    if diff.endswith("*"):
        diff = list(diff)
        diff.pop()
        diff = "".join(diff)

    return diff


print(differentiate("971(x)^6"))

