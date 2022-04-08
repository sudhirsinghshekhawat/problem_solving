def max_product(arr):
    arr.sort()
    n = len(arr)
    product_1 = arr[0] * arr[1]
    product_2 = arr[n - 1] * arr[n - 2]

    if product_1 > product_2:
        return arr[0], arr[1]
    else:
        return arr[n - 1], arr[n - 2]


def max_product_1(arr):
    posa = 0
    posb = 0

    nega = 0
    negb = 0

    n = len(arr)

    for i in range(n):
        if arr[i] > posa:
            posb = posa
            posa = arr[i]
        elif arr[i] > posb:
            posb = arr[i]

        if arr[i] < 0 and abs(arr[i]) > abs(nega):
            negb = nega
            nega = arr[i]

        elif arr[i] < 0 and abs(arr[i]) > abs(negb):
            negb = arr[i]

    if nega * negb > posa * posb:
        return nega, negb
    else:
        return posa, posb


arr = [-7, -6, 1, 2, 8, 9]
result = max_product(arr)
print(result)

result = max_product_1(arr)
print(result)
