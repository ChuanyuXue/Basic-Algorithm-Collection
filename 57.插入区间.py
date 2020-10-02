#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
from typing import *
# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = sorted(intervals + [newInterval], key=lambda x:x[0])
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

