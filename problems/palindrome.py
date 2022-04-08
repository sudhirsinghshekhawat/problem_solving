def is_palindrome(string):
    i = 0
    j = len(string) - 1
    while i <= j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


print(is_palindrome("ABCBA"))
print(is_palindrome("ABCCBA"))
print(is_palindrome("ABCCBADA"))
