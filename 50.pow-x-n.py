#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def inline(n):
            if n == 0:
                return 1.0
            y = inline(n // 2)
            return y * y if n % 2 == 0 else y * y * x
        return inline(n) if n >= 0 else 1.0 / inline(-1 * n)
        
# @lc code=end

a = Solution()
#print(a.log(10))

print(a.myPow(2, -10))