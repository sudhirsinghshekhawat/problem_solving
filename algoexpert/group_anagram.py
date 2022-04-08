def group_anagram(words):
    anagrams = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return list(anagrams.values())


string = ["yo", "oy", "for", "rof", "flop", "lopf"]
results = group_anagram(string)
print(results)
