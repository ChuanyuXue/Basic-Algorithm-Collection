#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        for i in s:
            if not stack or i not in self.pair or\
             (i in self.pair and self.pair[i] != stack[-1]):
                stack.append(i)
            else:
                stack.pop(-1)
        return not stack

    pair = {
        ')':'(',
        '}':'{',
        ']':'['
    }
                
# @lc code=end

a = Solution()
print(a.isValid("()[]{}"))

