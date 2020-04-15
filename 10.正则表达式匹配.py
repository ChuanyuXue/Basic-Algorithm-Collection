#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
#
#   aab
# c*a*b
#
#
# @lc code=start
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         left_s, left_p = 0, 0
#         while True:
#             if left_s == len(s):
#                 return True
#             if left_p == len(p):
#                 return False
#             if s[left_s] == p[left_p] or p[left_p] == '.':
#                 left_s = left_s + 1
#                 left_p = left_p + 1
#             elif p[left_p] == '*' and \
#             (s[left_s] == p[left_p - 1] or p[left_p - 1] == '.'):
#                 if left_s + 1 < len(s) and s[left_s] != s[left_s + 1]:
#                     left_s = left_s + 1
#                     left_p = left_p + 1
#                 else:
#                     left_s = left_s + 1
                
#             else:
#                 left_p = left_p + 1
#                 left_s = 0
#         return False   

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        # 第一个字母是否匹配
        first_match = bool(s and p[0] in {s[0],'.'})
        # 如果 p 第二个字母是 *
        if len(p) >= 2 and p[1] == "*":
            return self.isMatch(s, p[2:]) or \
            first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])
            
# @lc code=end
a = Solution()
print(a.isMatch('ab','.*c'))

