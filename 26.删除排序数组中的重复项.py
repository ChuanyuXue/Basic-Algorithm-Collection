#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#
from typing import *
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i != len(nums):
            if i != 0 and nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i = i + 1
        print(nums)
        return len(nums)

# @lc code=end

a = Solution()
print(a.removeDuplicates([1,1,2,2,5,5,5,7]))