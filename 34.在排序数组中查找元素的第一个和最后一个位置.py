#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from typing import *
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.binary_search(nums, 0, len(nums)-1, target)
    def binary_search(self, nums, left, right, target):
        mid = (left + right) // 2
        if left > right:
            return [-1, -1]
        elif nums[mid] == target:
            return self.find_scale(nums, mid, target)
        elif nums[mid] < target:
            return self.binary_search(nums, mid + 1, right, target)
        else:
            return self.binary_search(nums, left, mid - 1, target)

    def find_scale(self, nums, center, target):
        for i in range(center, len(nums)):
            if nums[i] == target:
                right = i
            else:
                break
        for i in range(center, -1, -1):
            if nums[i] == target:
                left = i
            else:
                break
        return [left, right]
# @lc code=end

a = Solution()
print(a.searchRange([1,2,3,4,5], -1))
