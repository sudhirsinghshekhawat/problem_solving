def reverse_words(string: str):
    return ' '.join(string.split()[::-1])


if __name__ == '__main__':
    string = "sudhir singh shekhawat"
    result = reverse_words(string)
    print(result)
