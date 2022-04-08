def fibonacci(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


def fib_dp_bottom_up(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    cache = [0 for _ in range(0, number + 1)]
    cache[1] = 1
    for i in range(2, number + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[number]


def fib_db_top_down(number, cache):
    if number == 0:
        return 0
    if number == 1:
        return 1
    if cache[number] != 0:
        return cache[number]
    result = fib_db_top_down(number - 1, cache) + fib_db_top_down(number - 2, cache)
    cache[number] = result
    return cache[number]


if __name__ == '__main__':
    print(fib_dp_bottom_up(5))
    number = 5
    cache = [0 for _ in range(number + 1)]
    cache[1] = 1
    print(fib_db_top_down(5, cache))
