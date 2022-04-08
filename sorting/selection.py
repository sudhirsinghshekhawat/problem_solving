def selection_sort(arr):
    for i in range(len(arr)):
        least = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[least]:
                least = j
        arr[i], arr[least] = arr[least], arr[i]


def main():
    arr = [11, 1, 17, 92, 23, 13]
    selection_sort(arr)
    print(arr)


if __name__ == '__main__':
    main()
