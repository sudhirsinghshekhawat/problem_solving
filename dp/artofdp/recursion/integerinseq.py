def is_int_in_seq(arr,i):
    if i == 0:
        return True
    return arr[i] == arr[i-1]+1 and is_int_in_seq(arr,i-1)


def main():
    arr1 = [1,2,3,4,5,6,7]
    print(is_int_in_seq(arr1,len(arr1)-1))

    arr2 = [1,2,3,4,5,7]
    print(is_int_in_seq(arr2,len(arr2)-1))





if __name__ == '__main__':
    main()


