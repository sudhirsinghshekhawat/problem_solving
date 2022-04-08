arr = [0] * 2


def binary(n):
    if n < 1:
        print(arr)
        return
    arr[n - 1] = 0
    binary(n - 1)
    arr[n - 1] = 1
    binary(n - 1)


binary(2)
