def sum_of_digit(num):
    if num == 0:
        return 0
    return num % 10 + sum_of_digit(num // 10)


def main():
    number = 1234
    print(sum_of_digit(number))


if __name__ == '__main__':
    main()
