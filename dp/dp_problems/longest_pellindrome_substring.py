result_start = 0
result_length = 0


def expand_range(string, start, end):
    while start >= 0 and end < len(string) and string[start] == string[end]:
        start -= 1
        end += 1
        global result_start
        global result_length

    if result_length < (end - start - 1):
        result_start = start + 1
        result_length = end - start - 1


def longest_palindrome_sub_string(string):
    str_length = len(string)
    if str_length < 2:
        return string
    for start in range(str_length):
        expand_range(string, start, start)
        expand_range(string, start, start + 1)
    return string[result_start: result_start + result_length]


def main():
    string1 = 'abcdefe'
    print(longest_palindrome_sub_string(string1))


if __name__ == '__main__':
    main()
