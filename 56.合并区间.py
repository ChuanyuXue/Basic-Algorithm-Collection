#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

from typing import *
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        index = 0
        while index < len(intervals) - 1:
            if intervals[index][1] >= intervals[index + 1][0]:
                intervals[index] = [intervals[index][0], 
                max(intervals[index][1], intervals[index+1][1])]
                del intervals[index + 1]
            else:
                index += 1
        return intervals
            

# @lc code=end

a = Solution()
print(a.merge([[1,4],[0,2],[3,5]]))
