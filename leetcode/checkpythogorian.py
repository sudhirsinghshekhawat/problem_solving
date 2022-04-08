def check_triplet(arr):
    n = len(arr)
    for i in range(n):
        arr[i] = arr[i] ** 2
    arr.sort()

    for i in range(n - 1, -1, -1):
        s = set()
        for j in range(i - 1, -1, -1):
            if (arr[i] - arr[j]) in s:
                return True
            s.add(arr[j])
    return False


if __name__ == '__main__':
    arr = [3, 2, 4, 6, 5]
    arr1 = [10, 4, 6, 12, 5]
    result = check_triplet(arr)
    print(result)
    result1 = check_triplet(arr1)
    print(result1)
