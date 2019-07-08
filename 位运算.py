'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

注意的是Python的int型数据是32位的
'''

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        count = 0
        if n < 0:
            n = 2**32 + n
        if n == 0:
            return 0
        if n == 1:
            return 1
        while n != 1:
            if n % 2:
                count += 1
            n = n // 2
        return count+1

