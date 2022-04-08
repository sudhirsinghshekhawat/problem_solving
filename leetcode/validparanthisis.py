class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack_list = []
        close_bracket_list = [')', '}', ']']
        close_bracket_hash = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in close_bracket_list and stack_list:
                pop_c = stack_list.pop()
                if not (pop_c == close_bracket_hash[ch]):
                    return False
            else:
                stack_list.append(ch)
        if stack_list:
            return False
        else:
            return True


if __name__ == '__main__':
    s = Solution()
    string = '()'
    print(s.isValid(string))
