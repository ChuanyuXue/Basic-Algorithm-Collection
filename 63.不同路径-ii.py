#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
from typing import *
# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for y in range(n)] for x in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        else:
            dp[0][0] = 0
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j - 1]
            else:
                dp[0][j] = 0
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]
            else:
                dp[i][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = 0
        return dp[m-1][n-1]
# @lc code=end
a = Solution()
print(a.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))
