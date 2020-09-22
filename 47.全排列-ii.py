#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
from typing import *
# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        back = []
        for i, v in enumerate(nums):
            back += [str([v] + x) for x in
             self.permuteUnique([x for k,x in enumerate(nums) if k != i])]
        return [eval(x) for x in set(back)]
# @lc code=end

a = Solution()
print(a.permuteUnique([1,1,2]))

