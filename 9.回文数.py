#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        aa = list(str(x))
        bb = reversed(aa)
        if "".join(aa) == "".join(bb):
            return True
        else:
            return False
# @lc code=end

a = Solution()
print(a.isPalindrome(121))
