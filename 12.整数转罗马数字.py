#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def transform(self, number, index):
        basis = self.mapp[index]

        if number == 0:
            return ''
        elif number == 4 or number == 5 or number == 9:
            return self.mapp[number * index]
        elif number < 5:
            return basis * number
        elif number > 5:
            return self.mapp[5 * index] + basis * (number - 5)


    def intToRoman(self, num: int) -> str:
        index = 0.1
        result = ''
        while num:
            right = int(num % 10)
            index = int(index * 10)
            num = num // 10
            result = self.transform(right, index) + result
        return result

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

a = Solution()
print(a.intToRoman(1994))

