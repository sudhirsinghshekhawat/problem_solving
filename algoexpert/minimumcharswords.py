from collections import Counter

input_string = ["this", "that", "did", "deed", "them", "a"]


def minimum_chars_words(arr):
    result = []
    for word in arr:
        counts = Counter(word)
        for key, val in dict(counts).items():
            result_counts = dict(Counter(result))
            char_count = result_counts.get(key, 0)
            if char_count < val:
                for _ in range(char_count, val):
                    result.append(key)
    return result


result = minimum_chars_words(input_string)
print(result)
