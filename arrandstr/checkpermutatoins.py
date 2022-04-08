def check_permutations(string1: str, string2: str) -> bool:
    if len(string1) != len(string2):
        return False

    if sorted(string1) != sorted(string2):
        return False
    return True


def check_permutations2(string1: str, string2: str) -> bool:
    char_set = [0] * 128
    for char in string1:
        char_set[ord(char)] = char_set[ord(char)] + 1

    for char in string2:
        char_set[ord(char)] = char_set[ord(char)] - 1
        if char_set[ord(char)] < 0:
            return False

    return True


if __name__ == '__main__':
    string1 = 'sudhir'
    string2 = 'rihdus'
    print(check_permutations(string1, string2))
    print(check_permutations2(string1, string2))



