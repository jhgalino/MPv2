import copy


def separateParts(function: str):
    assert function.count("~") == 2, "function.count('~') == 2"
    functionList = function.split("~")
    return functionList


def getParentheses(function: str):
    assert type(function) == str, "type(function) == str"
    assert function.count("(") >= 1, "function.count('(') >= 1"
    assert function.count(")") >= 1, "function.count(')') >= 1"

    startCounter = 0
    endCounter = 0
    functionList = list(function)
    for n in range(len(functionList)):
        if startCounter < 1 and functionList[n] == "(":
            functionList[n] = "~"
            startCounter += 1
    for n in range(len(functionList) - 1, -1, -1):
        if endCounter < 1 and functionList[n] == ")":
            functionList[n] = "~"
            endCounter += 1
    functionList = "".join(functionList)
    return functionList


def trig(func: list):
    assert len(func) == 3, "len(func) == 3"
    assert len(func[2]) == 0, "len(func[2]) == 0"
    assert len(func[0]) == 3, "len(func[0]) == 3"
    assert type(func[1]) == str, "type(func[1]) == str"
    assert type(func[0]) == str, "type(func[0]) == str"

    ans = ""
    if func[0] == "sin":
        ans = "(cos({}))".format(func[1])
    elif func[0] == "cos":
        ans = "(-sin({}))".format(func[1])
    elif func[0] == "sec":
        ans = "(sec({})tan({}))".format(func[1], func[1])
    elif func[0] == "csc":
        ans = "(-csc({})cot({}))".format(func[1], func[1])
    elif func[0] == "tan":
        ans = "(sec({})^2)".format(func[1])
    elif func[0] == "cot":
        ans = "(-csc({})^2)".format(func[1])

    return ans, func[1]


def coeff(func: list):
    assert len(func) == 3, "len(func) == 3"
    assert len(func[0]) >= 1, "len(func[0]) >= 1"

    exponent = 1
    if len(func[2]) == 2:
        func[2] = list(func[2])
        func[2].pop(0)
        func[2] = int("".join(func[2]))
        exponent = copy.deepcopy(func[2])
        func[2] -= 1
        if func[2] in [1, 0]:
            func[2] = ""
        else:
            func[2] = "^" + str(func[2])

    func[0] = int(func[0]) * exponent
    ans = "{}({}){}".format(func[0], func[1], func[2])
    return ans, func[1]


def exp(func: list):
    assert len(func[0]) == 0, "len(func[0]) == 0"
    assert len(func[2]) in [2, 0], "len(func[0]) == 0"
    if len(func[2]) == 2:
        func[2] = list(func[2])
        func[2].pop(0)
        func[2] = int("".join(func[2]))
        coefficient = copy.deepcopy(func[2])
        func[2] -= 1
        if func[2] in [1, 0]:
            func[2] = ""
        else:
            func[2] = "^" + str(func[2])
    ans = "{}({}){}".format(coefficient, func[1], func[2])
    return ans, func[1]


def chooseMethod(fxnList: list):
    assert len(fxnList) == 3, "len(fxnList) == 3"
    assert type(fxnList[0]) == str, "type(fxnList[0]) == str"
    assert type(fxnList[2]) == str, "type(fxnList[2]) == str"
    assert len(fxnList[0]) in [3, 1, 0], "len(fxnList[0]) in [3,1,0]"
    assert len(fxnList[2]) in [2, 0], "len(fxnList[2]) in [2, 0]"
    if len(fxnList[0]) == 3:
        return trig(fxnList)
    elif len(fxnList[0]) == 1:
        return coeff(fxnList)
    elif len(fxnList[0]) == 0:
        return exp(fxnList)


def differentiate(fxn: str):
    assert type(fxn) == str, "type(fxn) == str"
    if fxn == "(x)":
        return "1"
    else:
        answer, nextTerm = chooseMethod(separateParts(getParentheses(fxn)))
        assert type(answer) == str, "type(answer) == str"
        assert type(nextTerm) == str, "type(nextTerm) == str"
        if nextTerm == "x":
            return "{}".format(answer)
        else:
            return "'{}'".format(answer + "*" + differentiate(nextTerm))


OTHER_RECURSIVE_FUNCTIONS = [
    "chooseMethod",
    "exp",
    "coeff",
    "trig",
    "getParentheses",
    "separateParts",
]

