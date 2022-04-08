from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not magazine:
            return False

        if not ransomNote:
            return False

        if len(ransomNote) > len(magazine):
            return False

        rnote_counter = Counter(ransomNote)
        magzine_counter = Counter(magazine)
        print(rnote_counter)

        for element in rnote_counter:
            if magzine_counter[element] < rnote_counter[element]:
                return False
        return True

    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        for l in ransomNote:
            if l not in magazine:
                return False
            magazine = magazine.replace(l, '', 1)
        return True


if __name__ == '__main__':
    s = Solution()
    ransomNote = "a"
    magazine = "b"
    result = s.canConstruct(ransomNote, magazine)
    print(result)
    result = s.canConstruct1(ransomNote, magazine)
    print(result)
