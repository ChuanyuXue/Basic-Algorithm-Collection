#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
from typing import *
# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        lenth = len(nums)
        i = 0
        min_dis = 1e8
        location = None
        while i < lenth - 2:
            if i != 0 and nums[i] == nums[i - 1]:
                i = i + 1
                continue
            
            left = i + 1
            right = lenth - 1
            while left  < right:
                summ = nums[i] + nums[left] + nums[right]
                dis = target - summ
                if dis == 0:
                    return target
                if abs(dis) < min_dis:
                    min_dis = abs(dis)
                    location = summ
                if left < right and dis > 0:
                    left = left + 1
                if left < right and dis < 0:
                    right = right - 1
            i = i + 1
        return location
            
            

# @lc code=end

a = Solution()
print(a.threeSumClosest([-1,2,1,-4], 1))