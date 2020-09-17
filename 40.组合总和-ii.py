#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
from typing import *
# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return [[]]
        if len(candidates) == 0 or (target != 0 and target < min(candidates)):
            return []
        solvable = set()
        for loc, i in enumerate(candidates):
            if target >= i:
                back = self.combinationSum2([x for k,x in enumerate(candidates) if k != loc]
                , target - i)
                if back:
                    for each_solution in back:
                        solvable.add(str(sorted(each_solution + [i])))
        return [eval(x) for x in list(solvable)]
# @lc code=end

a = Solution()
print(a.combinationSum2([1], 2))
