#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
from typing import *
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        current_pos = 0
        count = 0
        while current_pos != len(nums) - 1:
            max_step = nums[current_pos]
            next_max = -1
            pos_max = -1
            if current_pos + max_step >= len(nums) - 1:
                return count + 1
            for next_pos in range(current_pos+1, \
                current_pos + max_step + 1):
                if next_pos + nums[next_pos] > next_max:
                    next_max = next_pos + nums[next_pos]
                    pos_max = next_pos
            current_pos = pos_max
            count += 1
        return count
# @lc code=end

a = Solution()
print(a.jump([1,2,1,1,1]))

