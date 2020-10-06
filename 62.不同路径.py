#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for y in range(n)] for x in range(m)]
        for j in range(0, n):
            dp[0][j] = 1
        for i in range(0, m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]
# @lc code=end

a = Solution()
print(a.uniquePaths(3,2))