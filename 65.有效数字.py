#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        numbers = [str(i) for i in range(10)]
        n = len(s)
        
        e_show_up, dot_show_up, num_show_up, num_after_e = False, False, False, False
        
        for i in range(n):
            c = s[i]
            if c in numbers:
                num_show_up = True
                num_after_e = True
            elif c in ('+', '-'):
                if i > 0 and s[i-1] != 'e':
                    return False
            elif c == '.':
                if dot_show_up or e_show_up:
                    return False
                dot_show_up = True
            elif c == 'e':
                if e_show_up or not num_show_up:
                    return False
                e_show_up = True
                num_show_up = False
            else:
                return False
            
        return num_show_up and num_after_e

# 作者：cheng-zhi-charles
# 链接：https://leetcode-cn.com/problems/valid-number/solution/python3jue-dui-jian-ji-yi-dong-de-jie-fa-by-cheng-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end

