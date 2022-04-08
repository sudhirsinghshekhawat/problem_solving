def squared_array(arr):
    square_array = [0 for _ in arr]
    smaller_idx = 0
    larger_idx = len(arr) - 1

    for idx in reversed(range(len(arr))):
        smaller_value = arr[smaller_idx]
        larger_value = arr[larger_idx]

        if abs(larger_value) < abs(smaller_value):
            square_array[idx] = smaller_value * smaller_value
            smaller_idx += 1
        else:
            square_array[idx] = larger_value * larger_value
            larger_idx -= 1

    return square_array


if __name__ == '__main__':
    arr = [-4, 1, 2, 3, 4]
    square_array = squared_array(arr)
    print(square_array)
