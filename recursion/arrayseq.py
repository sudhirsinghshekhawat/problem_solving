def is_array_in_sequence(arr, length):
    if length <= 1:
        return True
    return (arr[length] == arr[length - 1] + 1) and is_array_in_sequence(arr, length-1)


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(is_array_in_sequence(arr, len(arr) - 1))


if __name__ == '__main__':
    main()
