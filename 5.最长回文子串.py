#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start



class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        lenth = len(s)
        flag = [[0] * lenth for x in range(lenth)]
        max_index = None
        for i in range(lenth):
            flag[i][i] = 1
            max_index = (i, i)
        for i in range(lenth - 1):
            if s[i] == s[i+1]:
                flag[i][i+1] = 1
                max_index = (i, i+1)
        for i in range(lenth - 2):
            for k in range(0, lenth - i - 2):
                if flag[k+1][k+1+i] and s[k] == s[k + i + 2]:
                    flag[k][k + i + 2] = 1
                    max_index = (k, k+i+2)
        return s[max_index[0]: max_index[1]+1]


# @lc code=end

a = Solution()
print(a.longestPalindrome("cbbd"))

