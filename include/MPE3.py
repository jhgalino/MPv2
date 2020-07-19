def differentiate(fxn: str) -> str:
    if fxn == "x":
        return "1"
    dividedFxn = getFirstLevel(fxn)
    coeffOrTrig: str = dividedFxn[0]
    exponent: str = dividedFxn[2]
    insideParentheses: str = dividedFxn[1]

    if coeffOrTrig.isalpha():
        ans = computeTrig(coeffOrTrig, insideParentheses)
        ans = ans + "*" + differentiate(insideParentheses)
        if ans.endswith("*1"):
            ans = list(ans)
            ans.pop()
            ans.pop()
            ans = "".join(ans)
        return ans
    if len(exponent) != 0:
        if len(coeffOrTrig) != 0 and coeffOrTrig.isnumeric():
            ans = computeExpWithCoeff(coeffOrTrig, insideParentheses, exponent)
            ans = ans + "*" + differentiate(insideParentheses)
            ans = ans.replace("^1", "")
            if ans.endswith("*1"):
                ans = list(ans)
                ans.pop()
                ans.pop()
                ans = "".join(ans)
            return ans
        else:
            ans = computeExpWithoutCoeff(insideParentheses, exponent)
            ans = ans + "*" + differentiate(insideParentheses)
            ans = ans.replace("^1", "")
            if ans.endswith("*1"):
                ans = list(ans)
                ans.pop()
                ans.pop()
                ans = "".join(ans)
            return ans

    if len(coeffOrTrig) == 0 and len(exponent) == 0:
        ans = "1" + "*" + differentiate(insideParentheses)
        ans = ans.replace("^1", "")
        if ans.endswith("*1"):
            ans = list(ans)
            ans.pop()
            ans.pop()
            ans = "".join(ans)
        return ans


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


def computeExpWithCoeff(coeff: str, inside: str, exp: str) -> str:
    cf = int(coeff)
    expnt = int(exp.replace("^", ""))
    cf = cf * expnt
    expnt -= 1
    return "{}({})^{}".format(cf, inside, expnt)


def computeExpWithoutCoeff(inside: str, exp: str) -> str:
    expnt = int(exp.replace("^", ""))
    cf = int(exp.replace("^", ""))
    expnt -= 1
    return "{}({})^{}".format(cf, inside, expnt)


OTHER_RECURSIVE_FUNCTIONS = [
    "getFirstLevel",
    "computeTrig",
    "computeExpWithCoeff",
    "computeExpWithoutCoeff",
]

print(differentiate("(x)"))
