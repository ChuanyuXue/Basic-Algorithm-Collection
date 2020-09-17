#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
from typing import *
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target != 0 and target < min(candidates):
            return []
        if target == 0:
            return [[]]
        solvable = set()
        for i in candidates:
            if target >= i:
                back = self.combinationSum(candidates, target - i)
                if back:
                    for each_solution in back:
                        solvable.add(str(sorted(each_solution + [i])))
        return [eval(x) for x in list(solvable)]
# @lc code=end


a = Solution()
print(a.combinationSum([2],1))
