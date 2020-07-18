def differentiate(fxn: str) -> str:
    dividedFxn = getFirstLevel(fxn)
    coeffOrTrig = dividedFxn[0]
    exponent = dividedFxn[2]
    insideParentheses = dividedFxn[1]
    if insideParentheses == "x":
        return "1"
    else:
        assert type(coeffOrTrig) == str
        assert type(exponent) == str
        assert type(insideParentheses) == str
        if coeffOrTrig.isalpha():
            ans = computeTrig(coeffOrTrig, insideParentheses)
            ans = ans + "*" + differentiate(insideParentheses)
            ans = ans.replace("1", "")
            if ans[-1] == "*":
                ans[-1] = ""
            return ans
        elif coeffOrTrig.isnumeric():
            


def getFirstLevel(function: str) -> list:
    indexOfOpen = function.find("(")
    indexOfClose = function.rfind(")")
    function = list(function)
    function[indexOfOpen] = "|"
    function[indexOfClose] = "|"
    function = "".join(function)
    assert function.count("|") == 2, "| != 2"  # assert division by 2
    return function.split("|")


def computeTrig(trig: str, inside: str) -> str:
    if trig == "sin":
        return "(cos({}))".format(inside)
    elif trig == "cos":
        return "(-sin({}))".format(inside)
    elif trig == "tan":
        return "(sec({})^2)".format(inside)
    if trig == "sec":
        return "(sec({})tan({}))".format(inside, inside)
    if trig == "csc":
        return "(-csc({})cot({}))".format(inside, inside)
    if trig == "cot":
        return "(-csc({})^2)".format(inside)
