#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import *
# @lc code=start
class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     nums = sorted(nums)
    #     lenth = len(nums)
    #     i = 0
    #     result = []
    #     while i != lenth:
    #         if i != 0 and nums[i] == nums[i - 1]:
    #             i = i + 1
    #             continue
    #         left = i + 1
    #         right = lenth - 1
    #         while left < right:
    #             summ = nums[left] + nums[right] + nums[i]
    #             if summ == 0:
    #                 result.append([nums[left], nums[right], nums[i]])
    #                 while left < right and nums[right] == nums[right - 1]:
    #                     right = right - 1
    #                 while left < right and nums[left] == nums[left + 1]:
    #                     left = left + 1
    #                 right = right - 1
    #                 left = left + 1
    #             elif summ < 0:
    #                 left = left + 1
    #             elif summ > 0:
    #                 right = right - 1
    #         i = i + 1
    #     return result
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        if len(set(nums)) == 1 and nums[0] == 0:
            return [[0, 0, 0]]
        target_hash = {-x: i for i, x in enumerate(nums)}
        res = []
        res_hash = {}
        for i, first in enumerate(nums):
            for j, second in enumerate(nums[i + 1:]):
                if first + second in target_hash:
                    target_index = target_hash[first + second]
                    if target_index == i or target_index == i + j + 1:
                        continue
                    row = sorted([first, second, nums[target_index]])
                    key = ",".join([str(x) for x in row])
                    if key not in res_hash:
                        res.append(row)
                        res_hash[key] = True
        return res        
# @lc code=end
                
         

a = Solution()
print(a.threeSum([-2,0,0,2,2]))

