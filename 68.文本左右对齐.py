#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#
from typing import *
# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ## 获取每行都有哪些单词
        sentenses = []        
        while words:
            total_letters = 0
            total_words = 0
            each_line = []
            while words and total_letters + total_words + len(words[0]) <= maxWidth :
                total_words += 1
                total_letters += len(words[0])
                each_line.append(words[0])
                words = words[1:]
            sentenses.append(each_line)

        ## 获取每两个单词之间填什么
        gaps = []
        for sentense in sentenses:
            gap = []
            number_of_gaps = len(sentense) - 1
            space_requirement = maxWidth - sum([len(i) for i in sentense])
            if number_of_gaps > 0:
                space_feed = space_requirement // number_of_gaps
                space_feed_more = space_requirement % number_of_gaps
                gap = [space_feed for i in range(number_of_gaps)]
                for i in range(space_feed_more):
                    gap[i] += 1
                gaps.append(gap)
            else:
                gaps.append([maxWidth - len(sentense[0])])
        
        ## 输出
        result = []
        for line_index, val in enumerate(sentenses):
            out = ''
            if line_index != len(sentenses) - 1:
                for col_index, word in enumerate(val):
                    out += word
                    if col_index < len(gaps[line_index]):
                        out += ' ' * gaps[line_index][col_index]
                result.append(out)
            else:
                for col_index, word in enumerate(val):
                    out += word + ' '
                out = out[:-1]
                if len(out) < maxWidth:
                    out += ' ' * (maxWidth - len(out))
                result.append(out)
                
        return result


a = Solution()

print(a.fullJustify(["ask   not   what","your country can","do  for  you ask","what  you can do","for your country"], 16))


# @lc code=end

