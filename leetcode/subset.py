from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    output = [[]]

    for num in nums:
        output += [curr + [num] for curr in output]

    return output


def subsets_using_backtrack(nums: List[int]) -> List[List[int]]:
    def backtrack(first=0, curr=[]):
        if len(curr) == k:
            output.append(curr[:])
            return
        for i in range(first, n):
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()

    output = []
    n = len(nums)
    for k in range(n + 1):
        backtrack()
    return output


if __name__ == '__main__':
    array = [1, 2, 3]
    result = subsets(array)
    print(result)

    result = subsets_using_backtrack(array)
    print(result)
