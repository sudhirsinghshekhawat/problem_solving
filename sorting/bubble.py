def bubble_sort(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):

            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]


def main():
    arr = [11, 1, 17, 92, 23, 13]
    bubble_sort(arr)
    print(arr)


if __name__ == '__main__':
    main()
