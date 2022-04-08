def selection_sort(array):
    current_idx = 0
    while current_idx < len(array)-1:
        smallest_idx = current_idx
        for i in range(current_idx+1, len(array)):
            if array[smallest_idx] > array[i]:
                smallest_idx = i
        array[current_idx], array[smallest_idx] = array[smallest_idx], array[current_idx]
        current_idx += 1
    return array


if __name__ == '__main__':
    array = [11, 1, 2, 34, 5, 78, 90, 9]
    selection_sort(array)
    print(array)
