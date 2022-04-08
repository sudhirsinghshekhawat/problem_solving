def is_palindrome(string, i, j):
    if i > j:
        return True
    return string[i] == string[j] and is_palindrome(string, i+1, j-1)


def main():
    string1 = "sudhir"
    print(is_palindrome(string1, 0, len(string1)-1))

    string2 = "madam"
    print(is_palindrome(string2, 0, len(string2)-1))


if __name__ == '__main__':
    main()
