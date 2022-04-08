from typing import List


def products_array(array: List[int]) -> List[int]:
    products = [1] * len(array)
    left_product = [1] * len(array)
    right_product = [1] * len(array)

    left_running_product = 1

    for i in range(len(array)):
        left_product[i] = left_running_product
        left_running_product *= array[i]

    right_running_product = 1
    for i in reversed(range(len(array))):
        right_product[i] = right_running_product
        right_running_product *= array[i]

    for i in range(len(array)):
        products[i] = left_product[i] * right_product[i]

    return products


if __name__ == '__main__':
    array = [2, 3, 1, 4, 5]
    result = products_array(array)
    print(result)
