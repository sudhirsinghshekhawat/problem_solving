from typing import List


class Solution:
    """
        example on the left: [1, 3, 0, 2]
        example on the right: [2, 0, 3, 1]
    """

    def solve_n_queens(self, n: int) -> List[List[str]]:
        solution_array = []  # type: ignore
        state_array = []  # type: ignore
        self.search(state_array, solution_array, n)
        return solution_array

    def is_valid_state(self, state, n):
        return len(state) == n

    def get_candidate(self, state, n):
        if not state:
            return range(n)

        position = len(state)
        candidate = set(range(n))

        for row, col in enumerate(state):
            candidate.discard(col)
            distance = position - row
            candidate.discard(col + distance)
            candidate.discard(col - distance)
        return candidate

    def search(self, state, solution, n):
        if self.is_valid_state(state, n):
            state_string = self.state_to_string(state, n)
            solution.append(state_string)
            return
        for candidate in self.get_candidate(state, n):
            state.append(candidate)
            self.search(state, solution, n)
            state.pop()

    def state_to_string(self, state, n):
        ret = []
        for i in state:
            string = '.' * i + 'Q' + '.' * (n - i - 1)
            ret.append(string)
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.solve_n_queens(4))
