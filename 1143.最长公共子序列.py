#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for x in range(len(text2))]
         for x in range(len(text1))]

        for i in range(0, len(text1)):
            if text1[i] == text2[0]:
                for k in range(i, len(text1)):
                    dp[k][0] = 1
                break
        for k in range(0, len(text2)):
            if text2[k] == text1[0]:
                dp[0] = [0] * (k) + [1] * (len(text2) - k)
                break

        for i in range(1, len(text1)):
            for k in range(1, len(text2)):
                if text1[i] == text2[k]:
                    dp[i][k] = dp[i-1][k-1] + 1
                else:
                    dp[i][k] = max(dp[i-1][k], dp[i][k-1])
        return dp[i][k]
# @lc code=end

a = Solution()
print(a.longestCommonSubsequence('bsbininm','jmjkbkjkv'))
