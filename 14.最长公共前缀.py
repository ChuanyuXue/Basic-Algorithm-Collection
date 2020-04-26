#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs or '' in strs:
            return ''
        lenth = min([len(x) for x in strs])
        for i in range(lenth):
            temp = strs[0][i]
            for word in strs[1:]:
                if word[i] != temp:
                    return word[:i]
        return min(strs, key=lambda x:len(x))

# @lc code=end
a = Solution()
print(a.longestCommonPrefix(['a','ab']))
