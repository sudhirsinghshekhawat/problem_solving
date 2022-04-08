def unordered_linear_search(arr, k):
    for i, val in enumerate(arr):
        if k == val:
            return i
    return -1


def ordered_linear_search(arr, k):
    for i, val in enumerate(arr):
        if val == k:
            return i
        if val > k:
            return -1
    return -1


def main():
    arr = [11, 2, 1, 3, 13, 45, 12, 1]
    index = unordered_linear_search(arr, 13)
    print(f'index of 13 is : {index}')
    index = unordered_linear_search(arr, 111)
    print(f'index of 111 is : {index}')

    ordered_arr = [11, 13, 14, 16, 21, 22, 26, 29]
    index = ordered_linear_search(ordered_arr, 12)
    print(f'index of 12 is : {index}')
    index = ordered_linear_search(ordered_arr, 21)
    print(f'index of 21 is : {index}')


if __name__ == '__main__':
    main()
