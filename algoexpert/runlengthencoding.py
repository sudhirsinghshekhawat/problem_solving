def run_length_encoding(string):
    last_char = string[0]
    current_count = 0
    result_string = []

    for ch in string:
        if ch != last_char or current_count == 9:
            result_string.append(str(current_count))
            result_string.append(last_char)
            current_count = 1
            last_char = ch
        else:
            current_count += 1
    result_string.append(str(current_count))
    result_string.append(last_char)

    return ''.join(result_string)


if __name__ == '__main__':
    string = "AAAAAAAAAAAAABBBBCCD"
    result = run_length_encoding(string)
    print(result)
