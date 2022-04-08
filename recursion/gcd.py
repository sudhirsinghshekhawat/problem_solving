def gcd(number1, number2):
    if number1 < 0:
        number1 = -1 * number1

    if number2 < 0:
        number2 = -1 * number2

    if number1 == number2:
        return number1

    return gcd(number1 - number2, number2) if number1 > number2 else gcd(number2 - number1, number1)


def main():
    print(f'GCD of 12 and 3 is : {gcd(12, 3)}')
    print(f'GCD of 12 and 3 is : {gcd(12, -3)}')
    print(f'GCD of 12 and 3 is : {gcd(12, 3)}')


if __name__ == '__main__':
    main()
