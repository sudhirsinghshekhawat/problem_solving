from curses.ascii import isalpha


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s_list = list(s)
        l = 0
        r = len(s_list) - 1
        while l < r:
            if isalpha(s_list[l]) and isalpha(s_list[r]):
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1
            elif not isalpha(s_list[l]):
                l += 1
            else:
                r -= 1
        return ''.join(s_list)


# Input: s = "ab-cd"
# Output: "dc-ba"
#
# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
#
# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"

if __name__ == '__main__':
    s = Solution()
    print(s.reverseOnlyLetters("ab-cd"))
    print(s.reverseOnlyLetters("a-bC-dEf-ghIj"))
    print(s.reverseOnlyLetters("Test1ng-Leet=code-Q!"))
