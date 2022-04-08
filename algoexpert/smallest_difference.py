def smallest_difference(array1: list, array2: list):
    array1.sort()
    array2.sort()
    smallest_pair = []
    smallest = float("inf")
    current = float("inf")
    idx_one = 0
    idx_two = 0

    while idx_one < len(array1) and idx_two < len(array2):
        first_number = array1[idx_one]
        second_number = array2[idx_two]

        if first_number < second_number:
            current = second_number - first_number
            idx_one += 1
        elif second_number < first_number:
            current = first_number - second_number
            idx_two += 1
        else:
            return [first_number, second_number]

        if current < smallest:
            smallest = current
            smallest_pair = [first_number, second_number]
    return smallest_pair


if __name__ == '__main__':
    array1 = [-1, 5, 10, 20, 28, 3]
    array2 = [26, 134, 135, 15, 17]
    smallest_pair = smallest_difference(array1, array2)
    print(smallest_pair)
