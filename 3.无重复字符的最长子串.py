#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start

def check(string):
    count_set = set()
    output = ''
    for alp in string:
        if alp in count_set:
            return len(output), string.index(alp)
        else:
            count_set.add(alp)
            output += alp
    return len(output), 999999

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlenth = 0
        i = 0
        if len(s) == 0:
            return 0
        while i != len(s):
            if len(s) - i > maxlenth:
                newlenth, pos = check(s[i:])
                if newlenth > maxlenth:
                    maxlenth = newlenth
                i += pos if pos != 0 else 1
            else:
                return maxlenth      


# @lc code=end

a = Solution()
a.lengthOfLongestSubstring(" ")

