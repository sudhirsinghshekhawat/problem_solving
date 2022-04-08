def count_max_chocolate(money, price, wrap):
    if money < price:
        return 0

    choc = money // price

    choc = choc + (choc - 1) // (wrap - 1)

    return choc


if __name__ == '__main__':
    result = count_max_chocolate(15, 1, 3)
    print(result)
