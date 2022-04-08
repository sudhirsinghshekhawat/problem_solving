def reverse_string_by_word(string):
    words = string.split()
    reverse = words[::-1]
    print(' '.join(reverse))


if __name__ == '__main__':
    reverse_string_by_word("Sudhir Singh Shekhawat")
