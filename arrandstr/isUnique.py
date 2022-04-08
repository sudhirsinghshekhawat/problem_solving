def is_unique(string: str) -> bool:
    """
    finding the unique character in list
    """
    characters_dict = {}  # type: ignore
    for char in string:
        if characters_dict.get(char):
            return False
        characters_dict[char] = characters_dict.get(char, 0) + 1

    return True


def is_unique_chars(string: str):
    char_set = [False] * 128

    for char in string:
        if char_set[ord(char)]:
            return False
        char_set[ord(char)] = True
    return True


if __name__ == '__main__':
    string = 'sudhir'
    print(is_unique(string))
    print(is_unique_chars(string))
