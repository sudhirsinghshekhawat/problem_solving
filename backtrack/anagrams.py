import itertools


class Solution:

    def using_built_in_function(self, string):
        permutations = [''.join(param) for param in itertools.permutations(string)]
        print(permutations)

    def all_permutations(self, string, answer):
        if len(string) == 0:
            print(answer, sep=' ')

        for i in range(len(string)):
            ch = string[i]
            left_substr = string[0:i]
            right_substr = string[i + 1:]
            rest = left_substr + right_substr
            self.all_permutations(rest, answer + ch)


if __name__ == '__main__':
    s = Solution()
    s.using_built_in_function('abc')
    answer = ''
    s.all_permutations('abc', answer)
