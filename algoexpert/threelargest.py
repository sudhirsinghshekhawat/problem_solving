def find_three_largest(array):
    three_largest = [None, None, None]
    for num in array:
        update_three_largest(three_largest, num)
    return three_largest


def update_three_largest(three_largest, num):
    if three_largest[2] is None or num > three_largest[2]:
        shift_and_update(three_largest, num, 2)
    elif three_largest[1] is None or num > three_largest[1]:
        shift_and_update(three_largest, num, 1)
    elif three_largest[0] is None or num > three_largest[0]:
        shift_and_update(three_largest, num, 0)


def shift_and_update(three_largest, num, idx):
    for i in range(idx+1):
        if i == idx:
            three_largest[i] = num
        else:
            three_largest[i] = three_largest[i+1]


if __name__ == '__main__':
    array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    three_largest = find_three_largest(array)
    print(three_largest)
