def sqrt(x):
    if x == 0 or x == 1:
        return x
    start = 1
    end = x
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == x:
            return mid
        elif (mid * mid) < x < ((mid + 1) * (mid + 1)):
            return mid + 1
        elif mid * mid < x:
            start = mid + 1
        else:
            end = mid - 1


if __name__ == '__main__':
    result = sqrt(16)
    print(result)

    result = sqrt(17)
    print(result)

    result = sqrt(26)
    print(result)

    result = sqrt(39)
    print(result)
