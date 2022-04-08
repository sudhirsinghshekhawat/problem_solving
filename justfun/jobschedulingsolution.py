from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        job_array = self.create_job_array(startTime, endTime, profit)
        result = self.max_profit(job_array)
        print(result)

    def create_job_array(self, startTime, endTime, profit):
        job_array = []
        for i in range(len(startTime)):
            job_array.append((startTime[i], endTime[i], profit[i]))
        return job_array

    def lates_non_conflict(self, arr, i):
        for j in range(i - 1, -1, -1):
            if arr[j][1]  <= arr[i - 1][0]:
                return j
            return -1

    def max_profit(self, job_array):
        arr = sorted(job_array, key=lambda x: x[1])
        print(arr)
        n = len(arr)
        table = [None] * n
        table[0] = arr[0][2]

        for i in range(1, n):
            inclusive_profit = arr[i][2]
            l = self.lates_non_conflict(arr, i)
            print(f"l = {l}")

            if l != -1:
                inclusive_profit += table[l]
                print(inclusive_profit)
            table[i] = max(table[i - 1], inclusive_profit)

        print(table)
        result = table[n - 1]

        return result


if __name__ == '__main__':
    startTime = [1, 2, 3, 4, 6]
    endTime = [3, 5, 10, 6, 9]
    profit = [20, 20, 100, 70, 60]
    solution = Solution()
    solution.jobScheduling(startTime, endTime, profit)


