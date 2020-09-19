#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
from typing import *
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        left_index, right_index = 0, len(height) - 1
        water_level = []
        level = 0
        while left_index < right_index:
            left_high, right_hight = height[left_index], height[right_index]
            last_level = level
            level = min(left_high, right_hight)
            water_this_level = [level - max(last_level, x) for x in height[left_index+1: right_index] if x < level]
            water_this_level = [x for x in water_this_level if x > 0]
            water_level.append(sum(water_this_level))
            while left_index < right_index and (left_high <= level or right_hight <= level):
                if left_high <= right_hight:
                    left_index += 1
                else:
                    right_index -= 1
                left_high, right_hight = height[left_index], height[right_index]
        return sum(water_level)
# @lc code=end

a = Solution()
print(a.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
#print(a.trap([4,2,3]))
