#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
from typing import *
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        back = []
        for i in nums:
            back += [[i] + x for x in self.permute([x for x in nums if x != i])]
        return back
# @lc code=end

a = Solution()
print(a.permute([1,2,3]))

