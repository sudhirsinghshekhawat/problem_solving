arr = [11, 1, 2, 3, 56, 6, 1, 9, ]


def pair_sum(arr: list, target_sum: int) -> bool:
    arr_set = set()
    for val in arr:
        if target_sum - val in arr_set:
            return True
        arr_set.add(val)
    return False


if __name__ == '__main__':
    print(pair_sum(arr, 12))
    print(pair_sum(arr, 82))
    print(pair_sum(arr, 65))
