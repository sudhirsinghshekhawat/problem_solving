import sys


def minimum_sub_sliding(arr, target):
    end = start = 0
    min = sys.maxsize
    total = 0

    while end < len(arr):
        total += arr[end]

        while total >= target:
            if (end - start + 1) < min:
                min = end - start + 1
            total -= arr[start]
            start += 1
        end += 1

    if min == sys.maxsize:
        return 0
    return min


if __name__ == '__main__':
    arr = [4, 3, 1, 2, 6, 8]
    result = minimum_sub_sliding(arr, 8)
    print(result)
