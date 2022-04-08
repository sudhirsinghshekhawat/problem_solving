def sum_exist(arr, k):
    val_dict = {}
    for i, num in enumerate(arr):
        if k - num in val_dict:
            return True
        else:
            val_dict[num] = i
    return False


def main():
    arr = [10, 15, 3, 7]
    k = 17
    print(sum_exist(arr, 17))


if __name__ == '__main__':
    main()
