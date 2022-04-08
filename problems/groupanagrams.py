# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]


def group_anagrams(str_arr):
    anagrams = {}
    sorted_arr = [''.join(sorted(word)) for word in str_arr]
    for i, value in enumerate(sorted_arr):
        if value in anagrams:
            anagrams[value].append(str_arr[i])
        else:
            anagrams[value] = [str_arr[i]]
    return list(anagrams.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(strs)
    print(result)
