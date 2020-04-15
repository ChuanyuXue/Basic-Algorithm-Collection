#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        x = list(str(x))
        for i in range(len(x)-1, 0, -1):
            if x[i] == '0':
                x.pop(i)
            else:
                break

        if x[0] != '-':
            result = eval(''.join(reversed(x)))
            return result if result < 2**31 - 1 else 0
        if x[0] == '-':
            result = eval(''.join(reversed(x[1:])))
            return -1 * result if result < 2**31 - 1 else 0

# @lc code=end

a = Solution()
print(a.reverse(120))

