l1 = []


def addStrings(num1: str, num2: str) -> str:
    l1 = [int(x) for x in num1]
    l2 = [int(x) for x in num2]
    l3 = []
    i = len(l1) - 1
    j = len(l2) - 1

    carry = 0
    sum = 0

    while i >= 0 or j >= 0:
        if i >= 0 and j >= 0:
            sum = l1[i] + l2[j] + carry
            i -= 1
            j -= 1
        elif i >= 0:
            sum = l1[i] + carry
            i -= 1
        elif j >= 0:
            sum = l2[j] + carry
            j -= 1
        carry = 0
        if sum >= 10:
            carry = sum // 10
        l3.insert(0, sum % 10)
    if carry > 0:
        l3.insert(0, carry)
    return ''.join(map(str, l3))


if __name__ == '__main__':
    num1 = "456"
    num2 = "77"
    print(addStrings(num1, num2))
