def longest_substring_without_repeating_char(string):
    chars = [0] * 128
    left = 0
    right = 0
    res = 0

    while right < len(string):
        r = string[right]
        chars[ord(r)] += 1

        while chars[ord(r)] > 1:
            left_char = string[left]
            chars[ord(left_char)] -= 1
            left += 1
        res = max(res, right - left + 1)
        right += 1
    return res


def length_longest_substring(string):
    if not string:
        return
    ans = 0
    mp = {}
    i = 0

    for j in range(len(string)):
        if string[j] in mp:
            i = max(mp[string[j]], i)
        ans = max(ans, j - i + 1)
        mp[string[j]] = j+1
    return ans


if __name__ == '__main__':
    string = "sudshsir"
    result = longest_substring_without_repeating_char(string)
    print(result)

    result = length_longest_substring(string)
    print(result)
