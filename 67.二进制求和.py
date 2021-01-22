#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [int(x) for x in list(a)][::-1]
        b = [int(x) for x in list(b)][::-1]
        result = []
        carry = 0
        for i in range(max(len(a), len(b))):
            current = 0
            if i < len(a):
                current += a[i]
            if i < len(b):
                current += b[i]
            current += carry

            if current == 3:
                carry = 1
                result.append(1)
            elif current == 2:
                carry = 1
                result.append(0)
            elif current == 1:
                carry = 0
                result.append(1)
            else:
                carry = 0
                result.append(0)
        if carry == 1:
            result.append(1)
        return "".join([str(x) for x in result[::-1]])
            
# @lc code=end

a = Solution()
print(a.addBinary("0","1"))