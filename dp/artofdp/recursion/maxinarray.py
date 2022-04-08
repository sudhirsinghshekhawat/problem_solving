def max_in_array(arr, i):
    if i == 0:
        return arr[0]
    return max(arr[i], max_in_array(arr, i-1))


def main():
    arr = [32, -1, 45, 67, 8, 90, 12, 11]
    print(max_in_array(arr,len(arr)))


if __name__ == '__main__':
    main()
