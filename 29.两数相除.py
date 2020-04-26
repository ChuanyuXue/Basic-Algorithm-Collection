#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a, b, r, t = abs(dividend), abs(divisor), 0, 1
        while a >= b or t > 1:
            if a >= b: 
                r += t 
                a -= b
                t += t
                b += b
            else: 
                t >>= 1
                b >>= 1
        return min((-r, r)[dividend ^ divisor >= 0], (1 << 31) - 1)
        
        
        
# @lc code=end

a = Solution()
print(a.divide(2147483647, 1))