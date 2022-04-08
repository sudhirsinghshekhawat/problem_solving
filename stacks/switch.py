def add(var1, var2):
    return var1 + var2


def sub(var1, var2):
    return var1 - var2


def mul(var1, var2):
    return var1 * var2


def div(var1, var2):
    return var1 / var2


def default(*args):
    return "Incorrect operation"


switcher = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}


def switch(operator, var1, var2):
    return switcher.get(operator, default)(var1, var2)


print(switch('(', 1, 2))
