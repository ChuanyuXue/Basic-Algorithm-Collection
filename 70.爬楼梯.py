#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        results = [1,2]
        for i in range(2, n):
            results.append(results[i - 2] + results[i - 1])
        return results[-1]
# @lc code=end

a = Solution()
print(a.climbStairs(44))