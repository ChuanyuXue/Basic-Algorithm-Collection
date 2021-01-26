#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.replace('/',' ').split()
        results = []
        for ins in path_list:
            if ins not in ['.','..']:
                results.append(ins)
            elif ins == '..':
                results = results[:-1]
        return '/' + '/'.join(results)
        
# @lc code=end
a = Solution()
print(a.simplifyPath('/a/../../b/../c//.//'))