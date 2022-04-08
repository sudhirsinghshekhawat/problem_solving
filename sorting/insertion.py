def insertion_sort(arr):
    for i in range(len(arr)):
        temp = arr[i]
        k = i
        while k > 0 and temp < arr[k - 1]:
            arr[k] = arr[k - 1]
            k -= 1
        arr[k] = temp


def main():
    arr = [11, 1, 17, 92, 23, 13]
    insertion_sort(arr)
    print(arr)


if __name__ == '__main__':
    main()
