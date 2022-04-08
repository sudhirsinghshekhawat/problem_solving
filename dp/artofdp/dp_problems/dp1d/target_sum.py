def _target_sum(nums, target, i, sum):
    if i == len(nums)-1:
        return 1 if sum == target else 0
    return _target_sum(nums, target, i + 1, sum + nums[i]) \
           + _target_sum(nums, target, i + 1, sum - nums[i])


def target_sum(nums, target):
    return _target_sum(nums, target, 0, 0)


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1, 1]
    target = 3
    print(target_sum(nums, target))
