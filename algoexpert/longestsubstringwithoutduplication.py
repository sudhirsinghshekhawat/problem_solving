string = "clementisacap"


def longest_substring_without_duplication(string):
    last_seen = {}
    longest = [0, 1]
    start_idx = 0
    for i, ch in enumerate(string):
        if ch in last_seen:
            start_idx = max(start_idx, last_seen[ch] + 1)
        if longest[1] - longest[0] < i + 1 - start_idx:
            longest = [start_idx, i + 1]
        last_seen[ch] = i
    return string[longest[0]:longest[1]]


result = longest_substring_without_duplication(string)
print(result)
