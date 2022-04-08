def decimal_to_binary(number):
    if number == 0:
        return 0
    return (number % 2) + (10 * decimal_to_binary(number // 2))


def main():
    number = 5
    print(decimal_to_binary(number))


if __name__ == '__main__':
    main()
