#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
from typing import *
# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = [int(x) for x in 
        str(eval("".join([str(x) for x in digits])) + 1 )]
        result = [0] * (len(digits) - len(result)) + result
        return result
# @lc code=end

a = Solution()
print(a.plusOne([1,2,3]))

