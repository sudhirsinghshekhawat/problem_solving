from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:

        n = len(releaseTimes)
        max_val = releaseTimes[0]
        max_time_key = keysPressed[0]

        for i in range(len(releaseTimes) - 1):
            if releaseTimes[i + 1] - releaseTimes[i] > max_val:
                max_val = releaseTimes[i + 1] - releaseTimes[i]
                max_time_key = keysPressed[i + 1]

            elif releaseTimes[i + 1] - releaseTimes[i] == max_val:
                max_val = releaseTimes[i + 1] - releaseTimes[i]
                max_time_key = max(keysPressed[i], keysPressed[i + 1])

        return max_time_key


if __name__ == '__main__':
    s = Solution()
    input_list = [12, 23, 36, 46, 62]
    keys = "spuda"
    print(s.slowestKey(input_list, keys))
