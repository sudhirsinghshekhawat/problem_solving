for i in range(2, 3):
    print(i)
print('doneR')


def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    if len(nums) == 0:
        return [[]]
    nums_dict = {}
    for num in nums:
        nums_dict[num] = nums_dict.get(num, 0) + 1

    result = [[]]
    for x in nums_dict:
        n = len(result)
        for i in range(n):
            for j in range(1, nums_dict[x]+1):
                r = result[i] + [x] * j
                result.append(r)
    return result
