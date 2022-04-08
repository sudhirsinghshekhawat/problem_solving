from typing import List


def longest_common_prefix(strings: List[str]):
    if "" in strings or strings == []:
        return ""
    prefix = strings[0]

    for i in range(1, len(strings)):
        while prefix != "":
            try:
                if str.index(str(strings[i]), prefix) == 0:
                    break
                else:
                    prefix = prefix[:-1]
            except:
                prefix = prefix[:-1]

    return prefix


strings = ["flower", "flow", "flight"]
result = longest_common_prefix(strings)
print(result)

