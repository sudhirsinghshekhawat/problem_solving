class Solution:
    def is_valid(self, target):
        return target == 0

    def get_candidates(self, arr, start):
        return range(start, len(arr))

    def search(self, arr, partial, start, target):
        if self.is_valid(target):
            print(partial)
            return

        if start == len(arr):
            return

        for i in self.get_candidates(arr, start):
            candidate = arr[i]
            if candidate > target or (i > start and candidate == arr[i - 1]):
                continue
            partial.append(candidate)
            self.search(arr, partial, i + 1, target - candidate)
            partial.pop()

    def solve(self, arr, target):
        total = 0
        partial = []
        self.search(arr, partial, total, target)


if __name__ == '__main__':
    arr = [10, 1, 2, 7, 6, 1, 5]
    s = Solution()
    s.solve(arr, 8)
