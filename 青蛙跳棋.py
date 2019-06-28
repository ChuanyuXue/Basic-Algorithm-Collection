# -*- coding:utf-8 -*-
'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

解题思路，本来甚至想用深搜去做的，这玩意其实就是个斐波那契数列，因为跳上第N阶总由 跳上第N-2阶和跳上第N-1阶的数量的和组成
斐波那契数列非递归的思路，每次算后一个数等于前两个数的加和，用list更加清晰明了
'''

class Solution:
    def jumpFloor(self, number):
        temp = [1, 2]
        if number == 1:
            return temp[0]
        if number == 2:
            return temp[1]
        for i in range(number):
            temp.append(temp[-2] + temp[-1])
        return(temp[number-1])
