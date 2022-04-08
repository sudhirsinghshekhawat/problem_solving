def counting_sort(arr, k):
    b = [0 for el in arr]
    c = [0 for el in range(k + 1)]
    for i in range(k + 1):
        c[i] = 0
    for j in range(0, len(arr)):
        c[arr[j]] += 1
    for i in range(1, k + 1):
        c[i] += c[i - 1]
    for j in range(len(arr) - 1, -1, -1):
        tmp = arr[j]
        tmp2 = c[tmp] - 1
        b[tmp2] = tmp
        c[tmp] = c[tmp] - 1
    return b


def main():
    arr = [5, 1, 2, 2, 3]
    print(counting_sort(arr, 5))


if __name__ == '__main__':
    main()
