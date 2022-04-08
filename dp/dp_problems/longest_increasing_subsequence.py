def longest_increasing_sub_sequence(num_list):
    lis_table = [1]
    for i in range(len(num_list)):
        lis_table.append(1)
        for j in range(0, i):
            if num_list[i] > num_list[j] and lis_table[i] <= lis_table[j]:
                lis_table[i] = 1 + lis_table[j]

    print(lis_table)
    return max(lis_table)


def main():
    arr = [3, 2, 6, 4, 5, 1]
    print(longest_increasing_sub_sequence(arr))


if __name__ == '__main__':
    main()
