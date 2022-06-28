"""
Input: s = "aab"
Output: 0

Input: s = "aaabbbcc"
Output: 2
"""
import pytest


def min_char_deletion(string):
    frequency_count = {}
    deletion_count = 0

    for ch in string:
        frequency_count[ch] = frequency_count.get(ch, 0) + 1
    pq = list(frequency_count.values())
    pq.sort()

    while pq:
        frequency = pq.pop()
        if not pq:
            return deletion_count
        if frequency == pq[-1]:
            if frequency > 1:
                pq.append(frequency - 1)
            deletion_count += 1
        pq.sort()
    return deletion_count


@pytest.mark.parametrize("input,output", [("aab", 0), ("aaabbbcc", 2)])
def test_min_char_deletion(input, output):
    assert output == min_char_deletion(input)
    ...
