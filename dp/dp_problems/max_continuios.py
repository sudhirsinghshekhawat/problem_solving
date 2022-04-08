def max_contigous_sum(arr):
    max_sum = 0
    n = len(arr)
    for i in range(1, n):
        for j in range(i, n):
            curr_sum = 0
            for k in range(i, j + 1):
                curr_sum += arr[k]
                if curr_sum > max_sum:
                    max_sum = curr_sum
    return max_sum


def max_contigous_sum_1(arr):
    max_sum = 0
    n = len(arr)
    for i in range(1, n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum > max_sum:
                max_sum = curr_sum
    return max_sum


def can_complete_tour(self, petrol, cost):
    min_val = float('inf')
    min_pos = -1
    petrol_till_now = 0
    for i in range(0, petrol):
        petrol_till_now += petrol[i] - cost[i]
        if petrol_till_now < min_val:
            min_val = petrol_till_now
            min_pos = i
        if petrol_till_now >= 0:
            return (min_pos + 1) % len(petrol)
        return -1


def max_contigous_sum_dp1(arr):
    max_sum = 0
    n = len(arr)
    M = [0] * (n + 1)
    if arr[0] > 0:
        M[0] = arr[0]
    for i in range(1, n):
        if M[i - 1] + arr[i] > 0:
            M[i] = M[i - 1] + arr[i]
        else:
            M[i] = 0
    for i in range(0, n):
        if M[i] > max_sum:
            max_sum = M[i]
    return max_sum


def main():
    arr = [-2, 3, -16, 100, -4, 5]
    print(max_contigous_sum(arr))
    print(max_contigous_sum_1(arr))
    print(max_contigous_sum_dp1(arr))


if __name__ == '__main__':
    main()
