def merge_2_sorted_array(array1, array2):
    if not array1:
        return array2

    if not array2:
        return array1

    merged_array = [None] * (len(array1) + len(array2))

    i = j = k = 0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            merged_array[k] = array1[i]
            i += 1
        else:
            merged_array[k] = array2[j]
            j += 1

        k += 1

    while i < len(array1):
        merged_array[k] = array1[i]
        i += 1
        k += 1

    while j < len(array2):
        merged_array[k] = array2[j]
        j += 1
        k += 1

    return merged_array


if __name__ == '__main__':
    arr1 = [6, 7, 8]
    arr2 = []

    result = merge_2_sorted_array(arr1, arr2)
    print(result)
