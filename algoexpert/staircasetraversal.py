def stair_case_traversal(height, max_steps):
    dp = [0 for _ in range(height + 1)]
    dp[0] = 1
    dp[1] = 1

    for current_height in range(2, height + 1):
        for step in range(max_steps):
            dp[current_height] += dp[current_height - (step + 1)]
    return dp[height]


if __name__ == '__main__':
    result = stair_case_traversal(4, 2)
    print(result)
