def permutation(input_list, partial, used):
    if len(partial) == len(input_list):
        print(partial)
    else:
        for i in range(0, len(input_list) - 1):  # type:ignore
            if not used[i] and not (input_list[i] == input_list[i - 1] and not used[i - 1]):
                used[i] = True
                partial.append(input_list[i])
                permutation(input_list, partial, used)
                used[i] = False
                partial.pop()


def permute(arr, l, r):
    if l == r:
        print(arr)
        return
    else:
        for i in range(l, r + 1):
            arr[i], arr[l] = arr[l], arr[i]
            permute(arr, l + 1, r)
            arr[l], arr[i] = arr[i], arr[l]


def main():
    arr = [1, 2, 3]
    #used = [False for i in range(len(arr))]
    #partial = [1]
    #permutation(arr, partial, used)
    permute(arr,0,len(arr)-1)


if __name__ == '__main__':
    main()
