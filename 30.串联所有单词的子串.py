#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#
from typing import *
# @lc code=start
# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         if not words:
#             return []
#         target_lenth = len(''.join(words))
#         index_dict = {}
#         for i in range(0, len(s) - target_lenth + 1:
#             part_word = s[i: i + target_lenth]
#             if part_word not in index_dict:
#                 index_dict[part_word] = [i]
#             else:
#                 index_dict[part_word].append(i)
#         candidates = self.trace_back(words)
#         result = []
#         for i in candidates:
#             if i in index_dict:
#                 result = result + index_dict[i]
#         return result
    
#     def trace_back(self, words):
#         if len(words) == 1:
#             return [words[0]]
#         result = []
#         for i, v in enumerate(words):
#             get_from_higher = self.trace_back([x for k,x in enumerate(words) if k != i])
#             get_from_higher = [v + x for x in get_from_higher]
#             result.append(get_from_higher)
#         result = [x for y in result for x in y]
#         return list(set(result))

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        compare_dict = {}
        for i in words:
            if i not in compare_dict:
                compare_dict[i] = 0
            compare_dict[i] += 1
        target_lenth = len(''.join(words))
        word_lenth = len(words[0])
        result = []
        for i in range(0, len(s) - target_lenth + 1):
            part = s[i: i + target_lenth]
            new_dict = {}
            for k in range(0, len(part) - word_lenth + 1, word_lenth):
                each_word = part[k: k + word_lenth]
                if each_word not in compare_dict or \
                    (each_word in new_dict and new_dict[each_word] + 1 > compare_dict[each_word]):
                    break
                else:
                    if each_word not in new_dict:
                        new_dict[each_word] = 0
                    new_dict[each_word] += 1
            else:
                result.append(i)
        return result


    
# @lc code=end

a = Solution()
print(a.findSubstring("barfoothefoobarman", ["foo","bar"]))

