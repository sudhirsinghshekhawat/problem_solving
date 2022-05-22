class Solution:
    def countSubString(self, s:str) -> int:
        result = 0
        length = len(s)

        dp = [[False for _ in range(length)] for _ in range(length)]

        for i in range(length-1, -1, -1):
            dp[i][i] = True
            result += 1

            for j in range(i+1, length):
                if j-i == 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                else:
                    if s[i] == s[j] and dp[i+1][j-1] == True:
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                
                if dp[i][j] == True:
                    result +=1 
        return result


if __name__ == '__main__':
    solution = Solution()
    string = 'abc'
    result = solution.countSubString(string)
    print(result)
            

