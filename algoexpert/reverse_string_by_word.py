def reverse_string(string):
    if string is None:
        return
    reverse_words = []
    end_idx = len(string)
    print(end_idx)
    for idx in range(len(string) - 1, 0, -1):
        print(idx)
        if string[idx] == " ":
            reverse_words.append(string[idx + 1:end_idx])
            end_idx = idx
        print(reverse_words)
    reverse_words.append(string[0:end_idx])
    return " ".join(reverse_words)


if __name__ == '__main__':
    string = "sudhir singh SHEKHAWAT"
    result = reverse_string(string)
    print(result)
