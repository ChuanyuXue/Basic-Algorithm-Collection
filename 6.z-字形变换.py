#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s
        if numRows == 2:
            s = list(s)
            result_1 = [x for i, x in enumerate(s) if i % 2 == 0]
            result_2 = [x for i, x in enumerate(s) if i % 2 == 1]
            return ''.join(result_1 + result_2)

        high = numRows
        weith = len(s) // (numRows * 2 - 2) * (1 + numRows - 2) + (1 + numRows - 2)
        space = [[None for x in range(weith)] for y in range(high)]
        index = 0

        for each_matrix in range(len(s) // (numRows * 2 - 2) + 1):
            start_col = each_matrix * (numRows - 1)
            for y in range(numRows):
                if index == len(s):
                    break
                space[y][start_col] = s[index]
                index += 1
            for y in range(numRows - 2):
                if index == len(s):
                    break
                space[numRows - y - 2][start_col + y + 1] = s[index]
                index += 1
            if index == len(s):
                break
        
        result = ''
        for y in range(high):
            for x in range(weith):
                if space[y][x]:
                    result = result + space[y][x]
        return result
# @lc code=end

a = Solution()
print(a.convert("PAYPALISHIRING", 3))

