def find_3_sum(arr, sum):
    n = len(arr)
    for i in range(n - 1):
        s = set()
        curr_sum = sum - arr[i]
        for j in range(i + 1, n):
            if (curr_sum - arr[j]) in s:
                print(f"Triplet is {arr[i]},{arr[j]},{curr_sum - arr[j]}")
            s.add(arr[j])


arr = [1, 4, 45, 6, 10, 8, 3, 9]
sum = 22
find_3_sum(arr, sum)
