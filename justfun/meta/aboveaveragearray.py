from typing import List


def above_avergae_subarrays(arr: List[int]) -> List[List[int]]:
    if not arr:
        return []
    elif len(arr) == 1:
        return [[1, 1]]

    res = []

    for i in range(1, len(arr) - 1):
        total = arr[i - 1] + arr[i]
        if is_bigger(arr, i - 1, i, total / 2):
            res.append([i, i + 1])
    res.append([1, len(arr)])
    max_ = max(arr)
    count = 0

    for i in range(len(arr)):
        if max_ < arr[i]:
            count += 1
        if count <= 1:
            res.append([arr.index(max_) + 1, arr.index(max_) + 1])
    return res


def is_bigger(arr: List[int], idx1: int, idx2: int, target: float) -> bool:
    for i in range(len(arr)):
        if i == idx1 or i == idx2:
            continue
        if arr[i] >= target:
            return False
    return True


if __name__ == '__main__':
    arr = [3, 4, 2]
    result = above_avergae_subarrays(arr)
    print(result)
