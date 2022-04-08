from typing import List


def shiftingLetters(S: str, shifts: List[int]) -> str:
    ans = []
    X = sum(shifts) % 26
    for i, c in enumerate(S):
        index = ord(c) - ord('a')

        ans.append(chr(ord('a') + (index + X) % 26))

        X = (X - shifts[i]) % 26
    return "".join(ans)


if __name__ == '__main__':
    s = 'aaa'
    shifts = [1, 2, 3]
    print(shiftingLetters(s, shifts))
    # s1 = [0 for _ in range(len(shifts))]
    # # for i in range(shifts):
    # # s[0] = chr(97 + (((ord(s[0]) + shifts[0]) - 97) % 26))
    # s = list(s)
    # for i in range(1, len(shifts) + 1):
    #     for j in range(i):
    #         s[j] = chr(97 + (((ord(s[j]) + shifts[i - 1]) - 97) % 26))
    # print(s)
