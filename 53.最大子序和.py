#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
from typing import *
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        log = -1e12
        summ = 0
        for i in nums:
            if i + summ > i:
                summ = i + summ
            else:
                summ = i
            if summ > log:
                log = summ
        return log
# @lc code=end

a = Solution()
print(a.maxSubArray([-2, -1]))
