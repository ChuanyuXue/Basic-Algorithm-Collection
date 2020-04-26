#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
from typing import *
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        target_hash = {target - x: i for i, x in enumerate(nums)}
        res = []
        res_hash = {}
        for i, first in enumerate(nums):
            for j, second in enumerate(nums[i + 1:]):
                for k, third in enumerate(nums[i + j + 2:]):
                    if first + second + third in target_hash:
                        target_index = target_hash[first + second + third]
                        if target_index == i or target_index == i + j + 1 or target_index == i + j + k + 2:
                            continue
                        row = sorted([first, second, third, nums[target_index]])
                        key = ",".join([str(x) for x in row])
                        if key not in res_hash:
                            res.append(row)
                            res_hash[key] = True
        return res        
# @lc code=end
a = Solution()
print(a.fourSum([1, 0, -1, 0, -2, 2],0))

