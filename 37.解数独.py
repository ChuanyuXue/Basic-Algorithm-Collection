#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
from typing import *
from copy import deepcopy
# @lc code=start
class Solution:
    col_disk = dict()
    row_disk = dict()
    block_disk = dict()


    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        temp = deepcopy(board)
        for row_i, row in enumerate(self.search(temp, 0, 0)):
            for col_i, v in enumerate(row):
                board[row_i][col_i] = v
        
    def search(self, board, row_i, col_i):
        if row_i > 8:
            return board
        elif board[row_i][col_i] == '.':
            aviable_values = set([str(x) for x in range(1, 10)])\
                 - set([board[x][col_i] for x in range(9)])\
                      - set(board[row_i]) - \
                          self.find_in_this_block(board, row_i, col_i)
            back_list = []
            for add_value in aviable_values:
                temp = deepcopy(board)
                temp[row_i][col_i] = add_value
                if col_i == 8:
                    back_list.append(self.search(temp, row_i+1, 0))
                else:
                    back_list.append(self.search(temp, row_i, col_i+1))
            for candidate in back_list:
                if type(candidate) == list:
                    return candidate
            return
        else:
            if col_i == 8:
                return self.search(board, row_i+1, 0)
            else:
                return self.search(board, row_i, col_i+1)
    
    def find_in_this_block(self, board, row, col):
        col = int(col) // 3 * 3
        row = int(row) // 3 * 3
        collect = set()
        for c in range(col, col + 3):
            for r in range(row, row + 3):
                collect.add(board[r][c])
        return collect
        

# @lc code=end

a = Solution()

b = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
#b = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
a.solveSudoku(b)
print(b)

