def reverse_integer(number):
    reverse_number = 0
    while number:
        reminder = number % 10
        reverse_number = reverse_number*10 + reminder
        number = number // 10
    return reverse_number


if __name__ == '__main__':
    number = -123
    reverse_number = reverse_integer(abs(number))
    if number < 0:
        reverse_number = -1 * reverse_number
    print(f"reverse number : {reverse_number}")
