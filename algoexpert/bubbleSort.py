def bubble_sort(array):
    for i in range(len(array)):
        print(array)
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def bubble_sort_optimized(array):
    swapped = False
    for i in range(len(array)):
        print(array)
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
    return array


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7]

    result = bubble_sort(array)
    print(result)
    print("------------------------")

    result = bubble_sort_optimized(array)
    print(result)
