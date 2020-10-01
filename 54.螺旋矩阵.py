#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
from typing import *
# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def top_level(mat):
            return mat[0], mat[1:]
        def right_level(mat):
            return [x[-1] for x in mat], [x[:-1] for x in mat]
        def bottom_level(mat):
            return mat[-1][::-1], mat[:-1]
        def left_level(mat):
            return [x[0] for x in mat][::-1], [x[1:] for x in mat]
        operation_list = [top_level, right_level, bottom_level, left_level]

        result = []
        opt_index = 0
        while matrix and matrix[0]:
            level, mat = operation_list[opt_index](matrix)
            result += level
            matrix = mat
            if opt_index == 3:
                opt_index = 0
            else:
                opt_index += 1
        return result
            

# @lc code=end

a = Solution()
print(a.spiralOrder([
[1],[2],[3]
]))