#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        back = self.countAndSay(n - 1)
        result = []
        i, count = 0, 1
        while i < len(back):
            if i + 1 == len(back) or back[i] != back[i + 1]:
                result.append(str(count) + back[i])
                count = 1
            else:
                count += 1
            i += 1
        return ''.join(result)

# @lc code=end

a = Solution()
print(a.countAndSay(5))
