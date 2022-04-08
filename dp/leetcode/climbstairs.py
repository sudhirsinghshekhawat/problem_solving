def climb_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp = [0 for _ in range(n + 1)]

    for i in range(3, n + 1):
        ...
