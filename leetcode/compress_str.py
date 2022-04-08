def compress_string(string):
    if string is None:
        return ''
    last = string[0]
    count = 1
    result = ""
    for i in range(1, len(string)):
        if string[i] == last:
            count += 1
        else:
            result += last
            if count != 1:
                result += str(count)

            last = string[i]
            count = 1
    result += last
    if count != 1:
        result += str(count)

    return result


if __name__ == '__main__':
    string = "aaabbccdsa"
    result = compress_string(string)
    print(f"result : {result}")
