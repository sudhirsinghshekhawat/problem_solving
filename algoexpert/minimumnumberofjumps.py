# time complexity = O(n^2) and space complexity = O(n)
def minimum_jumps_to_reach(array):
    jumps = [float("inf") for x in range(len(array))]
    jumps[0] = 0

    for i in range(1, len(array)):
        for j in range(i):
            if array[j] + j >= i:
                jumps[i] = min(jumps[i], jumps[j] + 1)
    return jumps[-1]


# time complexity = O(n) and space Complexity O(n)
def minimum_number_of_jumps(array):
    if len(array) == 0:
        return 0
    jumps = 0
    steps = array[0]
    max_reach = array[0]

    for i in range(1, len(array) - 1):
        max_reach = max(max_reach, i + array[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = max_reach - i
    return jumps + 1


def minimum_number_jumps_1(array):
    jumps = 0
    current_jump_end = 0
    farthest_jump = 0

    for i in range(len(array)-1):
        farthest_jump = max(farthest_jump, i + array[i])
        if i == current_jump_end:
            jumps += 1
            current_jump_end = farthest_jump
    return jumps


if __name__ == '__main__':
    # array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
    # minimum_jumps = minimum_jumps_to_reach(array)
    # print(f"minimum number of jumps : {minimum_jumps}")
    # minimum_jumps = minimum_number_of_jumps(array)
    # print(f"minimum number of jumps : {minimum_jumps}")

    array = [1, 3, 2, 0, 2]
    result = minimum_number_of_jumps(array)
    print(result)

    result = minimum_number_jumps_1(array)
    print(result)
