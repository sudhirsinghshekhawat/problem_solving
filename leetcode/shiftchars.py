from typing import List


class Solution:

    def shifting_letters(self, s: str, shifts: List[int]) -> str:
        shifting_letters = []
        total_shifts = sum(shifts)
        for i, char in enumerate(s):
            index = ord(char) - ord('a')
            new_char = ord('a') + ((index + total_shifts) % 26)
            shifting_letters.append(chr(new_char))
            total_shifts = (total_shifts - shifts[i]) % 26
        return ''.join(shifting_letters)


if __name__ == '__main__':
    s = Solution()
    result = s.shifting_letters("abc", [3, 5, 9])
    print(result)
