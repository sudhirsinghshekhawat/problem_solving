def move_element_to_the_end(array, element):
    left = 0
    right = len(array) - 1

    while left < right:
        while left < right and array[right] == element:
            right -= 1
        while left < right and array[left] != element:
            left += 1
        array[left], array[right] = array[right], array[left]
        # left += 1
        # right -= 1


if __name__ == '__main__':
    array = [1, 2, 1, 4, 5, 6, 2, 1, 4, 7, 1, 1, 2, 1]
    move_element_to_the_end(array, 2)
    print(array)
