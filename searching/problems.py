import sys
from collections import OrderedDict


def max_repeatations(arr):
    arr_dict = {}
    max_val = arr[0]
    counter = 0
    for i, val in enumerate(arr):
        arr_dict[val] = arr_dict.get(val, 0) + 1
        if arr_dict[val] > counter:
            counter = arr_dict[val]
            max_val = val
    return max_val, counter


def first_repeat_element(arr):
    arr_dict = OrderedDict()
    for i, val in enumerate(arr):
        arr_dict[val] = arr_dict.get(val, 0) + 1
    for k, v in arr_dict.items():
        if v > 1:
            return k
    return -sys.maxsize


def first_repeat_element_1(arr):
    arr_dict = {}
    first_repeat = 0
    counter = -sys.maxsize
    for i, val in enumerate(arr):
        if arr_dict.get(val):
            arr_dict[val] = - arr_dict[val]
            if arr_dict[val] > counter:
                first_repeat = val
                counter = arr_dict[val]
        arr_dict[val] = i + 1
    return first_repeat


def find_missing_number(arr):
    for i, val in enumerate(arr, 1):
        if i != val:
            return i
    return -1


def find_missing_number_1(arr):
    x = 0
    for i in range(1, len(arr) + 2):
        x = x ^ i
    for i in arr:
        x = x ^ i
    return x


def main():
    arr = [211, 12, 13, 14, 211, 211, 12, 13, 14]
    # val, count = max_repeatations(arr)
    # print(f'max val : {val} and count is : {count}')
    # first_repeat = first_repeat_element(arr)
    # print(f'first repeat : {first_repeat}')
    first_repeat = first_repeat_element_1(arr)
    print(f'first repeat : {first_repeat}')

    # arr = [1, 2, 3, 4, 5, 7, 8, 9]
    # missing_number = find_missing_number(arr)
    # print(f'missing number : {missing_number}')
    # missing_number = find_missing_number_1(arr)
    # print(f'missing number : {missing_number}')


if __name__ == '__main__':
    main()
