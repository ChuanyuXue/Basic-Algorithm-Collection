#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#
from copy import deepcopy
# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        def check(mat, row, col):
            for i in range(n):
                if mat[row][i] == 'Q' or mat[i][col] == 'Q':
                    return False
            for i in range(1, n):
                if row + i < n and col + i < n and mat[row+i][col+i] == 'Q':
                    return False
                if row - i >= 0 and col - i >= 0 and mat[row-i][col-i] == 'Q':
                    return False
                if row + i < n and col - i >= 0 and mat[row+i][col-i] == 'Q':
                    return False
                if row - i >= 0 and col + i < n and mat[row-i][col+i] == 'Q':
                    return False
            return True
                
        def backtrace(mat, row_index):
            if row_index == n:
                return [mat]
            else:
                result = []
                for col_index in range(0, n):
                    temp = deepcopy(mat)
                    if check(mat, row_index, col_index):
                        line = temp[row_index]
                        temp[row_index] = line[:col_index] + 'Q' + line[col_index+1:]
                        result += [x for x in backtrace(temp, row_index + 1)]
                return result
        
        init_mat = ["".join(['.' for x in range(n)]) for y in range(n)]
        return len(backtrace(init_mat, 0))


# @lc code=end

