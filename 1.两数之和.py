#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from typing import List

# @lc code=start
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i, a in enumerate(nums):
#             for k, b in enumerate(nums[i+1: ]):
#                 if a + b == target:
#                     return [i, k + i + 1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {x:i for i, x in enumerate(nums)}
        for i, a in enumerate(nums):
            finded = target - a
            if finded in mapping and mapping[finded] != i:
                return [i, mapping[finded]]
# @lc code=end



