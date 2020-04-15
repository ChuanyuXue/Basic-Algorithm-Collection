#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        remapp = dict(zip(self.mapp.values(), self.mapp.keys()))
        thound, handred, ten, one = None, None, None, None
        for i, v in enumerate(s):
            if v in ['D', 'C']:
                thound = i
        for i, v in enumerate(s):
            if v in ['L', 'X']:
                handred = i
        for i, v in enumerate(s):
            if v in ['L', 'X']:
                ten = i
        for i, v in enumerate(s):
            if v in ['V', 'I']:
                one = i
        

    mapp = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

# @lc code=end

