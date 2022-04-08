arr = [0, 1, 1, 2]


def remove_duplicates(arr, val):
    index = -1
    for i in range(len(arr)):
        if arr[i] == val:
            index = i
            break
        i += 1
    index += 1
    while index < len(arr) and arr[index] == val :
        del arr[index]
        index += 1
    print(arr)


remove_duplicates(arr, 1)
