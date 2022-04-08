def compress_string(string: str):
    length = len(string)
    last = string[0]
    count = 1
    compressed_str = ''
    for i in range(1, length):
        if string[i] == last:
            count = count + 1
        else:
            compressed_str = compressed_str + last + str(count)
            last = string[i]
            count = 1
    print(compressed_str)


compress_string('ssjkkiii')
