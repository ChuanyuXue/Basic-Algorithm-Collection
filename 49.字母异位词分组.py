#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
from typing import *
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        root_hash = {}
        for s in strs:
            root = "".join(sorted(s))
            root_hash.setdefault(root,[])
            root_hash[root].append(s)
        return list(root_hash.values())
# @lc code=end

a = Solution()
print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))