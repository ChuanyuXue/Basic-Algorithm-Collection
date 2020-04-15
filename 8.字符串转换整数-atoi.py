#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def deminish_zero(self, s):
        if s[0] == '+':
            s = s[1:]
        for i,v in enumerate(s):
            if v != '0':
                s = s[i:]
                break
        return s

    def myAtoi(self, str: str) -> int:
        s = list(str)
        if str == '+' or str == '-' or str == '':
            return 0

        for i,v in enumerate(s):
            if v != ' ':
                s = s[i:]
                break
        
        v = s[0]
        if not (v == '+' or v == '-' or '0' <= v <= '9'):
            return 0
        
        for i,v in enumerate(s):
            if (i == 0 and v in ['+','-']):
                continue
            if ('9' < v or v < '0'):
                s = s[:i]
                break
        if len(s) > 1:
            v = s[1]
            if not (v == '.' or '0' <= v <= '9'):
                return 0
        if len(s) == 1 and not ('0' <= s[0] <= '9'):
            return 0

        if s[0] == '-':
            result = eval("".join(self.deminish_zero(s[1:])))
            if result <= 2**31:
                return -1 * result
            else:
                return -1 * 2**31
        else:
            result = eval("".join(self.deminish_zero(s)))
            if result <= 2**31-1:
                return result
            else:
                return 2**31 - 1

        
             
# @lc code=end
a = Solution()
print(a.myAtoi("-5-"))
