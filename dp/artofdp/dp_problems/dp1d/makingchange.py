import sys

coins = [10, 6, 1]


def make_change(coin_sum):
    if coin_sum == 0:
        return 0
    minimum_coins = sys.maxsize
    currnet_minimum_coins = 0
    for coin in coins:
        if coin_sum - coin >= 0:
            currnet_minimum_coins = make_change(coin_sum - coin)
        if currnet_minimum_coins < minimum_coins:
            minimum_coins = currnet_minimum_coins
    return minimum_coins + 1


def make_change_cache(coin_sum, cache):
    if cache[coin_sum] >= 0:
        return cache[coin_sum]
    minimum_coins = sys.maxsize
    currnet_minimum_coins = 0
    for coin in coins:
        if coin_sum - coin >= 0:
            currnet_minimum_coins = make_change(coin_sum - coin)
        if currnet_minimum_coins < minimum_coins:
            minimum_coins = currnet_minimum_coins
        cache[coin_sum] = minimum_coins + 1
    return cache[coin_sum]


def make_change_top_down(coin_sum):
    cache = [-1 for _ in range(coin_sum + 1)]
    return make_change_cache(coin_sum, cache)


def make_change_bottom_up(coin_sum):
    cache = [0 for _ in range(coin_sum + 1)]
    for i in range(1, coin_sum + 1):
        minimum_coins = sys.maxsize

        for coin in coins:
            if i - coin >= 0:
                currnet_minimum_coins = cache[i - coin] + 1
                if currnet_minimum_coins < minimum_coins:
                    minimum_coins = currnet_minimum_coins

        cache[i] = minimum_coins
    return cache[coin_sum - 1]


if __name__ == '__main__':
    min_coin = make_change(13)
    print(min_coin)

    min_coin = make_change_top_down(13)
    print(min_coin)

    min_coin = make_change_bottom_up(13)
    print(min_coin)
