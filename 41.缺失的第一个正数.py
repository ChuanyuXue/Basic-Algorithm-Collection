#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
from typing import *
# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] if nums[i] > 0 else len(nums) + 1
        for i, v in enumerate(nums):
            v = abs(v)                
            if v <= len(nums) and nums[v - 1] > 0:
                nums[v - 1] = -1 * nums[v - 1]
        for i, v in enumerate(nums):
            if v > 0:
                return i + 1
        return len(nums) + 1
# @lc code=end


a = Solution()
print(a.firstMissingPositive([1,1]))