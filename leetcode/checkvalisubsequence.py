def is_valid_sub_sequence(array, sequence_arr):
    seq_idx = 0
    for value in array:
        if seq_idx == len(sequence_arr):
            break
        if value == array[seq_idx]:
            seq_idx += 1
    return len(sequence_arr) == seq_idx


def main():
    array = [1, 2, 4, 5, 6, 7, 9]
    sequence = [2, 4, 7]
    print(is_valid_sub_sequence(array, sequence))


if __name__ == '__main__':
    main()
