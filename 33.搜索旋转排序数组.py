#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
from typing import *

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while right >= left:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] >= nums[0]:
                if nums[0] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and target <= nums[len(nums) - 1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
# @lc code=end

a =Solution()
x = [4,5,6,7,0,1,2]
for i in x:
    print(a.search(x, i))
print(a.search([4,5,6,7,0,1,2],3))
print(a.search([5,1,2,3,4],4))
print(a.search([5],4))
print(a.search([5],5))

