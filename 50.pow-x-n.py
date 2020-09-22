#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            result = 1
            for i in range(0, n):
                result *= x
            return round(result, 5)
        else:
            result = 1
            for i in range(0, -1 * n):
                result *= x
            return round(1 / result, 5)
        
# @lc code=end

a = Solution()
print(a.myPow(0.00001, 2147483647))