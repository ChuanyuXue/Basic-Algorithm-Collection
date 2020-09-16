#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#
from typing import *
# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_disk = dict()
        row_disk = dict()
        block_disk = dict()
        for row_i, row in enumerate(board):
            for col_i, v in enumerate(row):
                if v == '.':
                    continue
                block = self.block_map(row_i, col_i)
                col_disk.setdefault(col_i, set())
                row_disk.setdefault(row_i, set())
                block_disk.setdefault(block, set())

                if v in col_disk[col_i]:
                    return False
                else:
                    col_disk[col_i].add(v)
                if v in row_disk[row_i]:
                    return False
                else:
                    row_disk[row_i].add(v)
                if v in block_disk[block]:
                    return False
                else:
                    block_disk[block].add(v)
        return True


    def block_map(self, row, col):
        return str(row // 3) + str(col // 3)
# @lc code=end

a = Solution()
print(a.isValidSudoku(
  [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))

