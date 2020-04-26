#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
from typing import *
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return self.table[digits[0]]
        else:
            result = []
            for i in self.table[digits[0]]:
                result.append(
                    [i + x for x in self.letterCombinations(digits[1:])]
                    )
            result = [i for j in result for i in j]
            return result

    table = {
        '1': [''],
        '2': ['a','b','c'],
        '3': ['d','e','f'],
        '4': ['g','h','i'],
        '5': ['j','k','l'],
        '6': ['m','n','o'],
        '7': ['p','q','r','s'],
        '8': ['t','u','v'],
        '9': ['w','x','y','z']
    }

# @lc code=end
a = Solution()
print(a.letterCombinations("23"))
