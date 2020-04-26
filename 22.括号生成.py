#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

from typing import *

# @lc code=start
class Solution:
    def generate(self, n):
        if n == 1:
            return [')']
        else:
            result = []
            for i in ['(',')']:
                result.append([i + x for x in self.generate(n - 1) ]) 
            return [x for y in result for x in y]

    def check(self, s):
        stack = []
        for i in s:
            if stack and stack[-1] + i == '()':
                stack.pop(-1)
            else:
                stack.append(i)
                
        return not stack

    def generateParenthesis(self, n: int) -> List[str]:
        return ['(' + x for x in self.generate(n * 2 - 1) if self.check('(' + x)]
# @lc code=end

a = Solution()
print(a.generateParenthesis(3))