#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#
from typing import *
# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for v in nums:
            if v > 0:
                if nums[v - 1] > 0:
                    nums[v - 1] = -1 * nums[v - 1]
            else:
                if nums[-1 * v - 1] > 0:
                    nums[-1 * v - 1] = -1 * nums[-1 * v - 1]
        result = []
        for i, v in enumerate(nums):
            if v > 0:
                result.append(i + 1)
        return result
# @lc code=end

a = Solution()
print(a.findDisappearedNumbers([1,1]))