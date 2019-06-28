# -*- coding:utf-8 -*-
'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
'''

class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for i in range(n//2):
            a += b
            b += a
        return b if n%2 else a
         
class Solution:
    def Fibonacci(self, n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b
        return a
