from curses.ascii import isalpha

s1 = "A man, a plan, a canal: Panama"
s2 = "0P"


def is_pellindrome(s: str):
    s1 = ''
    for ch in s:
        if isalpha(ch):
            s1 += ch.lower()
    return s1 == s1[::-1]


print(is_pellindrome(s1))
print(is_pellindrome(s2))
