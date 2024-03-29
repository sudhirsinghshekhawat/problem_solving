from collections import Counter
from typing import List

"""
Class for finding the anagrams
finding the group of anagrams 
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        function for finding anagrams
        """
        ns, np = len(s), len(p)
        if ns < np:
            return []
        p_count = Counter(p)
        s_count = Counter()

        output = []

        for i in range(ns):
            s_count[s[i]] += 1
            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1

            if p_count == s_count:
                output.append(i - np + 1)

        return output


s = "cbaebabacd"
p = "abc"
solution = Solution()
result = solution.findAnagrams(s, p)
print(result)
